"""Download the PhysioNet records used throughout the book into book/data/.

Run from the repository root:

    python scripts/download_data.py

All records come from PhysioNet (https://physionet.org) and are distributed under
open licenses; see book/data/README.md for the source and citation of each one.
"""
from __future__ import annotations

import time
import urllib.request
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "book" / "data"

# database -> list of files to fetch (paths relative to the database root)
FILES = {
    # MIT-BIH Arrhythmia Database: two-lead ambulatory ECG, 360 Hz, 30 min
    "mitdb": [f"{r}.{ext}" for r in ["100", "105", "106", "119", "203", "208"]
              for ext in ("hea", "dat", "atr")],
    # MIT-BIH Noise Stress Test Database: pure noise records
    "nstdb": [f"{r}.{ext}" for r in ["bw", "em", "ma"] for ext in ("hea", "dat")],
    # EEG Motor Movement/Imagery Database: 64-channel EEG, 160 Hz
    "eegmmidb/1.0.0/S001": [f"S001R{run:02d}.edf" for run in (1, 2, 3, 4)],
    # Examples of Electromyograms: needle EMG, 4 kHz
    "emgdb": [f"emg_{k}.{ext}" for k in ("healthy", "myopathy", "neuropathy")
              for ext in ("hea", "dat")],
    # BIDMC PPG and Respiration Dataset: ECG, PPG, impedance respiration, 125 Hz
    "bidmc": [f"bidmc{r:02d}.{ext}" for r in (1, 2, 3) for ext in ("hea", "dat", "breath")],
    # Abdominal and Direct Fetal ECG Database: 4 abdominal + 1 direct lead, 1 kHz
    "adfecgdb": ["r01.edf", "r01.edf.qrs"],
    # Long-term beat annotations only (no raw signal) for HRV and complexity analysis
    "nsrdb": ["16265.hea", "16265.atr"],
    "chfdb": ["chf01.hea", "chf01.ecg"],
}

# Folder name on disk for each database key
FOLDER = {"eegmmidb/1.0.0/S001": "eegmmidb"}
BASE_URL = "https://physionet.org/files"


def url_for(db: str, filename: str) -> str:
    path = db if "/" in db else f"{db}/1.0.0"
    return f"{BASE_URL}/{path}/{filename}"


def download_file(url: str, dest: Path, attempts: int = 4) -> None:
    for k in range(attempts):
        try:
            tmp = dest.with_suffix(dest.suffix + ".part")
            urllib.request.urlretrieve(url, tmp)
            tmp.rename(dest)
            return
        except Exception as exc:  # network hiccups on the PhysioNet side
            if k == attempts - 1:
                raise RuntimeError(f"could not download {url}: {exc}") from exc
            time.sleep(3 * (k + 1))


def fetch(db: str, files: list[str]) -> None:
    target = DATA / FOLDER.get(db, db)
    target.mkdir(parents=True, exist_ok=True)
    missing = [f for f in files if not (target / Path(f).name).exists()]
    if not missing:
        print(f"{db:22s} up to date")
        return
    for f in missing:
        download_file(url_for(db, f), target / Path(f).name)
    print(f"{db:22s} downloaded {len(missing)} file(s)")


def main() -> None:
    for db, files in FILES.items():
        fetch(db, files)
    total = sum(p.stat().st_size for p in DATA.rglob("*") if p.is_file())
    print(f"\nData folder: {DATA}  ({total / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
