#!/usr/bin/env python3
"""Frozen feasibility calculations for the Candidate Muon-Lag Extension.

This script does not fit FPM parameters. It writes the two predeclared lifetime
curves, a summary-data Gaussian likelihood, an event-time exponential
likelihood, and beam/precision requirements for gamma bins spanning the cap.
"""

from __future__ import annotations

import hashlib
import json
import math
import subprocess
import tempfile
from pathlib import Path
from typing import Iterable


PROJECT = Path(__file__).resolve().parents[1]
OUTPUT = PROJECT / "outputs" / "muon_lag_protocol_predictions.json"

C_LIGHT_M_S = 299_792_458.0
MUON_MASS_MEV_C2 = 105.6583755
MUON_REST_LIFETIME_S = 2.1969811e-6
GAMMA_CAP = 31.873862947240752
GAMMA_BINS = (20.0, 29.3, 32.0, 40.0, 100.0)
Z_DISCOVERY = 5.0

REFERENCE_DOWNLOADS = {
    "pdg_2025_muon_listing.pdf": "https://pdg.lbl.gov/2025/listings/rpp2025-list-muon.pdf",
    "fermilab_conf_16_424_g2_beam.pdf": (
        "https://lss.fnal.gov/archive/2016/conf/fermilab-conf-16-424-ad.pdf"
    ),
    "fermilab_tm_2627_muon_test_beam.pdf": (
        "https://lss.fnal.gov/archive/test-tm/2000/fermilab-tm-2627-e.pdf"
    ),
}

REFERENCE_RECORDS = [
    {
        "record_id": "pdg_2025_rest_muon",
        "kind": "rest_lifetime",
        "gamma": 1.0,
        "lab_lifetime_us": 2.1969811,
        "uncertainty_us": 0.0000022,
        "role": "calibration",
        "likelihood_usable": False,
        "source_url": REFERENCE_DOWNLOADS["pdg_2025_muon_listing.pdf"],
        "notes": "Sets the candidate extension's rest-frame decay hazard only.",
    },
    {
        "record_id": "cern_storage_1977",
        "kind": "time_dilation_reference",
        "gamma": 29.33,
        "lab_lifetime_us": 64.378,
        "uncertainty_us": None,
        "role": "below_threshold_reference",
        "likelihood_usable": False,
        "source_url": "https://cds.cern.ch/record/133132",
        "notes": (
            "Published storage-ring lifetime reference; no machine-readable decay-time "
            "series or likelihood-ready uncertainty is retrieved by this script."
        ),
    },
    {
        "record_id": "ftbf_2016",
        "kind": "beam_capability",
        "gamma": 94.65,
        "lab_lifetime_us": None,
        "uncertainty_us": None,
        "role": "facility_feasibility",
        "likelihood_usable": False,
        "source_url": REFERENCE_DOWNLOADS["fermilab_tm_2627_muon_test_beam.pdf"],
        "notes": "Documents 10-50 GeV/c muon capability, not a decay-lifetime measurement.",
    },
]


def gamma_to_beta(gamma: float) -> float:
    if gamma < 1.0:
        raise ValueError("gamma must be at least one")
    return math.sqrt(1.0 - 1.0 / gamma**2)


def momentum_gev_c(gamma: float) -> float:
    return MUON_MASS_MEV_C2 * math.sqrt(gamma**2 - 1.0) / 1000.0


def tau_fpm_s(gamma_kin: float) -> float:
    return MUON_REST_LIFETIME_S * min(gamma_kin, GAMMA_CAP)


def tau_sr_s(gamma_kin: float) -> float:
    return MUON_REST_LIFETIME_S * gamma_kin


def gaussian_log_likelihood(tau_hat_s: float, sigma_s: float, tau_model_s: float) -> float:
    """Log likelihood for a reported lifetime estimate with Gaussian error."""
    if sigma_s <= 0.0:
        raise ValueError("summary lifetime uncertainty must be positive")
    return -0.5 * ((tau_hat_s - tau_model_s) / sigma_s) ** 2 - math.log(
        sigma_s * math.sqrt(2.0 * math.pi)
    )


def exponential_log_likelihood(decay_times_s: Iterable[float], tau_model_s: float) -> float:
    """Unbinned likelihood for accepted, background-subtracted decay times.

    A real analysis must replace this idealized form with its predeclared
    acceptance, background, loss, and momentum-spread model.
    """
    times = list(decay_times_s)
    if tau_model_s <= 0.0 or any(t < 0.0 for t in times):
        raise ValueError("decay times and model lifetime must be non-negative/positive")
    return -len(times) * math.log(tau_model_s) - sum(times) / tau_model_s


def required_events_for_five_sigma(gamma: float) -> float | None:
    """Ideal exponential-MLE count for a 5-sigma separation if SR is true.

    The standard error of the lifetime MLE is approximated by tau_SR/sqrt(N).
    This is planning-only and excludes all systematic uncertainties.
    """
    delta = tau_sr_s(gamma) - tau_fpm_s(gamma)
    if delta <= 0.0:
        return None
    return (Z_DISCOVERY * tau_sr_s(gamma) / delta) ** 2


def download_references(destination: Path) -> dict[str, dict[str, str | int]]:
    """Download reference PDFs into a temporary directory for provenance checks.

    The files are intentionally not retained in the repository. A failed
    download is recorded in the report; it does not create substitute data.
    """
    records: dict[str, dict[str, str | int]] = {}
    for filename, url in REFERENCE_DOWNLOADS.items():
        target = destination / filename
        try:
            subprocess.run(
                ["curl", "--fail", "--location", "--silent", "--show-error", "--output", str(target), url],
                check=True,
                capture_output=True,
                text=True,
                timeout=60,
            )
            records[filename] = {
                "url": url,
                "status": "downloaded_temporary",
                "bytes": target.stat().st_size,
                "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
            }
        except Exception as exc:  # report a provenance failure rather than hide it
            records[filename] = {"url": url, "status": "download_failed", "error": str(exc)}
    return records


def protocol_rows() -> list[dict[str, float | int | None]]:
    rows: list[dict[str, float | int | None]] = []
    for gamma in GAMMA_BINS:
        fpm = tau_fpm_s(gamma)
        sr = tau_sr_s(gamma)
        delta = sr - fpm
        rows.append({
            "gamma_kin": gamma,
            "beta": gamma_to_beta(gamma),
            "momentum_GeV_c": momentum_gev_c(gamma),
            "tau_FPM_us": fpm * 1e6,
            "tau_SR_us": sr * 1e6,
            "difference_us": delta * 1e6,
            "direct_flight_length_FPM_km": C_LIGHT_M_S * fpm / 1000.0,
            "direct_flight_length_SR_km": C_LIGHT_M_S * sr / 1000.0,
            "maximum_systematic_us_for_one_fifth_gap": delta * 1e6 / 5.0,
            "ideal_events_for_5sigma_if_SR_true": required_events_for_five_sigma(gamma),
        })
    return rows


def main() -> None:
    cap_beta = gamma_to_beta(GAMMA_CAP)
    with tempfile.TemporaryDirectory(prefix="fpm_muon_lag_") as temp_dir:
        downloads = download_references(Path(temp_dir))
        result = {
            "protocol_name": "Candidate Muon-Lag Extension feasibility audit",
            "status": "NO_PUBLIC_HIGH_GAMMA_DECAY_LIFETIME_DATA",
            "download_policy": "Reference PDFs are downloaded to a temporary directory and deleted after this run.",
            "frozen_model": {
                "motion_dictionary": "L(v_lab)=min[L_rest*gamma_kin(v_lab), L_max]",
                "fpm_curve": "tau_FPM=tau_mu*min(gamma_kin, gamma_cap)",
                "sr_baseline": "tau_SR=tau_mu*gamma_kin",
                "gamma_cap": GAMMA_CAP,
                "rest_lifetime_s": MUON_REST_LIFETIME_S,
                "muon_mass_MeV_c2": MUON_MASS_MEV_C2,
                "cap_beta": cap_beta,
                "cap_momentum_GeV_c": momentum_gev_c(GAMMA_CAP),
                "cap_lifetime_us": tau_fpm_s(GAMMA_CAP) * 1e6,
            },
            "gamma_bins": protocol_rows(),
            "likelihood": {
                "summary_data": "Gaussian log likelihood for a fitted tau_hat and declared sigma.",
                "event_time_data": "Ideal unbinned exponential log likelihood; acceptance, background, losses, and momentum spread must be declared before use.",
                "rejection_rule": "Reject the candidate extension when a preregistered high-gamma likelihood comparison significantly favors the uncapped SR baseline under the frozen uncertainty model.",
            },
            "feasibility": {
                "historical_storage_reference_gamma": 29.33,
                "historical_reference_below_cap": True,
                "existing_high_gamma_fit_data": False,
                "facility_note": "The temporary FTBF reference documents 10-50 GeV/c muon-beam capability, above the cap momentum, but not a controlled decay-lifetime dataset.",
                "measurement_requirement": "A storage ring or equivalently long time-resolved decay region is required; direct-flight lengths are listed per gamma bin.",
            },
            "temporary_reference_downloads": downloads,
            "reference_records": REFERENCE_RECORDS,
        }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(OUTPUT)
    print(f"cap momentum: {result['frozen_model']['cap_momentum_GeV_c']:.6f} GeV/c")
    print(f"cap lifetime: {result['frozen_model']['cap_lifetime_us']:.6f} us")
    print(f"status: {result['status']}")


if __name__ == "__main__":
    main()
