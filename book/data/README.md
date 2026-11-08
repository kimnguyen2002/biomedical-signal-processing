# Data used in this book

Every recording in this folder comes from [PhysioNet](https://physionet.org) {Goldberger et al., 2000} and is redistributed here unchanged so that the notebooks run offline. Each database is shared by PhysioNet under an open license (Open Data Commons Attribution License v1.0 for most of them); please consult the database page linked below and cite the original publication when you reuse the data.

To download the files again, run `python scripts/download_data.py` from the repository root.

| Folder | Database | Records | Sampling rate | Channels | Used for |
|---|---|---|---|---|---|
| `mitdb/` | [MIT-BIH Arrhythmia Database](https://physionet.org/content/mitdb/1.0.0/) (Moody & Mark, 2001) | 100, 105, 106, 119, 203, 208 (30 min each) | 360 Hz | MLII plus V1 or V5 (mV) | ECG analysis, QRS detection, beat classification |
| `nstdb/` | [MIT-BIH Noise Stress Test Database](https://physionet.org/content/nstdb/1.0.0/) (Moody et al., 1984) | `bw` baseline wander, `em` electrode motion, `ma` muscle artifact | 360 Hz | 2 noise channels (mV) | Realistic noise for filtering experiments |
| `eegmmidb/` | [EEG Motor Movement/Imagery Dataset](https://physionet.org/content/eegmmidb/1.0.0/) (Schalk et al., 2004) | Subject S001, runs R01 (eyes open), R02 (eyes closed), R03 (fist movement), R04 (fist imagery) | 160 Hz | 64 EEG channels, 10-10 system | EEG rhythms, alpha blocking, event-related desynchronization |
| `emgdb/` | [Examples of Electromyograms](https://physionet.org/content/emgdb/1.0.0/) | `emg_healthy`, `emg_myopathy`, `emg_neuropathy` | 4 kHz | 1 needle EMG channel (mV) | EMG morphology and spectra |
| `bidmc/` | [BIDMC PPG and Respiration Dataset](https://physionet.org/content/bidmc/1.0.0/) (Pimentel et al., 2017) | `bidmc01`, `bidmc02`, `bidmc03` (8 min each) | 125 Hz | ECG leads, PPG (`PLETH`), impedance respiration (`RESP`) | PPG analysis, pulse arrival time, respiration rate |
| `adfecgdb/` | [Abdominal and Direct Fetal ECG Database](https://physionet.org/content/adfecgdb/1.0.0/) (Jezewski et al., 2012) | `r01` (5 min) | 1 kHz | 1 direct fetal scalp lead, 4 abdominal leads | Fetal ECG extraction, source separation |
| `nsrdb/` | [MIT-BIH Normal Sinus Rhythm Database](https://physionet.org/content/nsrdb/1.0.0/) | `16265` beat annotations only (about 25 h) | 128 Hz | annotations only | Long-term heart rate variability |
| `chfdb/` | [BIDMC Congestive Heart Failure Database](https://physionet.org/content/chfdb/1.0.0/) (Baim et al., 1986) | `chf01` beat annotations only (about 20 h) | 250 Hz | annotations only | Heart rate variability in heart failure |

## Notes on reading the files

- WFDB records (`.hea` header, `.dat` signal, annotation files such as `.atr`) are read with the [`wfdb`](https://github.com/MIT-LCP/wfdb-python) package: `wfdb.rdrecord("data/mitdb/100")` and `wfdb.rdann("data/mitdb/100", "atr")`.
- In the BIDMC records the channel names carry a trailing comma (`"PLETH,"`) and the channel order differs between records, so select channels by name after stripping the comma.
- EDF files (`eegmmidb`, `adfecgdb`) are read with [MNE-Python](https://mne.tools): `mne.io.read_raw_edf(...)`. The EEG channel names end with dots (`"Fc5."`); `mne.datasets.eegbci.standardize(raw)` converts them to standard 10-10 labels.
- The fetal QRS locations for `r01` are stored in `r01.edf.qrs` and can be read with `wfdb.rdann("data/adfecgdb/r01.edf", "qrs")`.
