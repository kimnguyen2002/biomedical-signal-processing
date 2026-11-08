# Biomedical Signal Processing

**From Fundamentals to Advanced Methods, with Python**  
Kim Nguyen

A growing set of English-language study notes on biomedical signal processing, with step-by-step mathematics, executable Python examples, and an emphasis on the ECG.

[Read the book](https://kimnguyen2002.github.io/biomedical-signal-processing/)

## Included material

This edition includes the existing lessons across foundations, systems, Fourier analysis, sampling, filtering, ECG physiology and noise, EEG fundamentals, and wavelets, together with the supporting appendices. Unfinished chapter outlines and placeholder sections have been omitted. Chapters, sections, and equations are numbered consecutively within this edition.

This is an independent working copy; the original project remains unchanged.

## Build the website

The ready-to-publish HTML is in `docs/`. Open `docs/index.html` to read the book locally.

After editing the notebooks or Markdown, regenerate it with:

```bash
python -m pip install -r requirements-build.txt
python scripts/build_site.py
```

This refreshes `docs/`, including the sidebar, figures, notebook downloads, and equation hover previews. Commit both the source changes and the updated `docs/` folder.

## Run the examples

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/download_data.py
jupyter lab book/
```

The data downloader retrieves the example recordings from PhysioNet; see [the dataset notes](book/data/README.md). Raw recordings are not included in this repository. Install the scientific packages required by the notebooks you want to run.

## Publish on GitHub Pages

Upload or push this project's contents, including `docs/` and `.github/`, to the repository's `main` branch. In **Settings → Pages → Build and deployment → Source**, choose **GitHub Actions**. The included workflow publishes the HTML in `docs/` whenever that folder changes on `main`.

The site will be available at [kimnguyen2002.github.io/biomedical-signal-processing](https://kimnguyen2002.github.io/biomedical-signal-processing/).

Keep local environments, raw datasets, source textbook PDFs, and temporary builds outside the commit. They are not required to serve the website. The optional PDF generator remains available separately.

## Project files

- `book/`: published lessons, chapter outlines, references, and website assets.
- `docs/`: ready-to-publish HTML and website assets.
- `scripts/`: website build, data download, equation previews, and optional PDF generation.
- `.github/workflows/`: website deployment.

Local environments, caches, raw recordings, build output are excluded from version control. Source textbook PDFs and course notes are kept outside the repository.

## License

Text: CC BY 4.0. Code: MIT. See [LICENSE.md](LICENSE.md).
