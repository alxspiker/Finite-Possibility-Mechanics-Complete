#!/usr/bin/env python3
"""Run the existing scalar SPARC bridge audit from verified temporary files.

The SPARC data are downloaded from Zenodo record 16284118 into a temporary
directory, checked against the record's published MD5 values, used once, and
deleted.  No data directory is retained in this repository.  The audit is a
retrospective scalar rotation-curve comparison; it is not a tensor-morphology
test and is not prospective physical evidence.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT = Path(__file__).resolve().parents[1]
SIMULATOR = PROJECT / "scripts" / "fpm_simulator.py"
OUTPUT = PROJECT / "outputs" / "sparc_reproducibility_audit.json"
ZENODO_API = "https://zenodo.org/api/records/16284118"
REQUIRED_FILES = {
    "SPARC_Lelli2016c.mrt": "6181df386bfc05868a3700c196e800da",
    "Rotmod_LTG.zip": "e4c8b92766026770ed35e5889064e12b",
}


def curl_to(url: str, target: Path) -> None:
    subprocess.run(
        ["curl", "--fail", "--location", "--silent", "--show-error", "--output", str(target), url],
        check=True,
        timeout=120,
        capture_output=True,
        text=True,
    )


def md5(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


def import_simulator() -> Any:
    spec = importlib.util.spec_from_file_location("fpm_sparc_audit", SIMULATOR)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {SIMULATOR}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="fpm_sparc_") as temporary:
        temp_dir = Path(temporary)
        metadata_path = temp_dir / "zenodo_record.json"
        curl_to(ZENODO_API, metadata_path)
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        remote_files = {entry["key"]: entry for entry in metadata["files"]}

        checked_files: dict[str, dict[str, str | int | bool]] = {}
        for name, expected_md5 in REQUIRED_FILES.items():
            if name not in remote_files:
                raise RuntimeError(f"Zenodo record does not contain required file: {name}")
            target = temp_dir / name
            source = remote_files[name]["links"]["self"]
            curl_to(source, target)
            actual_md5 = md5(target)
            expected_size = int(remote_files[name]["size"])
            checked_files[name] = {
                "url": source,
                "expected_md5": expected_md5,
                "actual_md5": actual_md5,
                "expected_bytes": expected_size,
                "actual_bytes": target.stat().st_size,
                "verified": actual_md5 == expected_md5 and target.stat().st_size == expected_size,
            }
            if not checked_files[name]["verified"]:
                raise RuntimeError(f"integrity check failed for {name}")

        with zipfile.ZipFile(temp_dir / "Rotmod_LTG.zip") as archive:
            archive.extractall(temp_dir)
        rotmod_dir = temp_dir / "Rotmod_LTG"
        if not rotmod_dir.is_dir():
            # The verified Zenodo package stores the rotation-model files at
            # its archive root. Stage that layout under the simulator's
            # historic directory contract, inside this disposable directory.
            root_rotmods = list(temp_dir.glob("*_rotmod.dat"))
            if not root_rotmods:
                raise RuntimeError("Rotmod_LTG.zip contained no *_rotmod.dat files")
            rotmod_dir.mkdir()
            for source in root_rotmods:
                source.rename(rotmod_dir / source.name)

        simulator = import_simulator()
        derived = simulator.derive_all(simulator.Axioms())
        old_data_dir = os.environ.get("FPM_SPARC_DATA_DIR")
        os.environ["FPM_SPARC_DATA_DIR"] = str(temp_dir)
        try:
            audit = simulator.audit_sparc_fpm_bridge(derived)
        finally:
            if old_data_dir is None:
                os.environ.pop("FPM_SPARC_DATA_DIR", None)
            else:
                os.environ["FPM_SPARC_DATA_DIR"] = old_data_dir
        # The simulator reports its live data directory for interactive use.
        # It would be a deleted temporary path in this persistent artifact, so
        # retain only the fact that a verified temporary source was used.
        audit.pop("data_dir", None)
        audit["data_dir_policy"] = "verified_temporary_directory_deleted_after_run"

        result = {
            "audit_name": "Verified temporary SPARC scalar bridge audit",
            "evidence_status": "REPRODUCIBLE_RETROSPECTIVE_SCALAR_BENCHMARK",
            "scope": (
                "This is an externally recoverable scalar rotation-curve benchmark. "
                "It is not a tensor-galaxy morphology prediction, a fitted model, or prospective evidence."
            ),
            "data_policy": "Zenodo source files were downloaded into a temporary directory and deleted after this run.",
            "source": {
                "record_doi": metadata.get("doi"),
                "record_url": "https://zenodo.org/records/16284118",
                "retrieved_utc": datetime.now(timezone.utc).isoformat(),
                "files": checked_files,
            },
            "frozen_ledger": {
                "parameter_fit": False,
                "sample": "Q=1 galaxies with at least five valid rotation-curve rows",
                "baryonic_velocity_composition": "v_gas^2 + 0.5*v_disk^2 + 0.7*v_bulge^2",
                "fpm_susceptibility": "nu_FPM(x)=1+Omega_max/sqrt(x+r_tensor)/(1+E_zombie*x^2)^beta",
                "comparison_baseline": "nu_RAR(x)=1/(1-exp(-sqrt(x)))",
                "summary_metric": "median per-galaxy RMSE in km/s",
            },
            "result": audit,
        }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(OUTPUT)
    print(f"Q=1 galaxies: {result['result']['galaxies_Q1']}")
    print(f"FPM gas-boundary median RMSE: {result['result']['rmse_FPM_gas_boundary_km_s']:.6f} km/s")
    print(f"RAR/MOND median RMSE: {result['result']['rmse_RAR_MOND_km_s']:.6f} km/s")


if __name__ == "__main__":
    main()
