"""Build the PDF edition of the book.

The book is first rendered as a single HTML page (Sphinx `singlehtml` builder), then
printed to PDF by headless Chromium through Playwright, so the PDF looks like the website:
same fonts, same figures, same mathematics.

Usage (from the repository root):

    python scripts/build_pdf.py            # build singlehtml, then print
    python scripts/build_pdf.py --no-build # print an existing singlehtml build

One-time setup:  pip install playwright && python -m playwright install chromium
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "book"
SINGLE = BOOK / "_build" / "singlehtml" / "index.html"
PDF = BOOK / "_build" / "pdf" / "biomedical-signal-processing.pdf"

# Software rendering keeps headless Chromium working inside sandboxes and CI runners.
CHROMIUM_ARGS = ["--use-angle=swiftshader", "--enable-unsafe-swiftshader",
                 "--disable-gpu-compositing", "--in-process-gpu"]

PRINT_CSS = """
@page { size: A4; margin: 16mm 15mm 18mm 15mm; }
html { font-size: 10.5pt !important; }
.bd-sidebar-primary, .bd-sidebar-secondary, .bd-header, .bd-header-article,
.bd-footer, .bd-footer-article, .bd-footer-content, .prev-next-area,
.headerlink, .bd-search, .search-button-field, .theme-switch-button,
#pst-back-to-top, .sidebar-toggle, .bd-sidebar { display: none !important; }
.bd-main, .bd-content, .bd-article-container, .bd-article, .bd-page-width {
  max-width: 100% !important; width: 100% !important; margin: 0 !important; padding: 0 !important;
}
section > h1 { break-before: page; }
section:first-of-type > h1 { break-before: auto; }
h1, h2, h3 { break-after: avoid; }
.cell_output img, figure, table, mjx-container[display="true"] { break-inside: avoid; }
div.highlight pre { white-space: pre-wrap !important; word-break: break-word; font-size: 8.5pt; }
details > summary { display: none !important; }
a { color: inherit !important; text-decoration: none !important; }
"""

FOOTER = ('<div style="font-size:8px;width:100%;text-align:center;color:#777;">'
          'Biomedical Signal Processing &middot; <span class="pageNumber"></span></div>')


def build_singlehtml() -> None:
    cmd = ["jupyter-book", "build", str(BOOK), "--builder", "singlehtml"]
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)


def print_pdf() -> None:
    if not SINGLE.exists():
        sys.exit(f"Missing {SINGLE}; run without --no-build first.")
    PDF.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(args=CHROMIUM_ARGS)
        page = browser.new_page(viewport={"width": 1100, "height": 1400})
        page.goto(SINGLE.resolve().as_uri(), wait_until="load", timeout=600_000)
        page.add_style_tag(content=PRINT_CSS)
        page.evaluate("document.querySelectorAll('details').forEach(d => d.open = true)")
        page.emulate_media(media="print")
        t0 = time.time()
        page.wait_for_function("window.MathJax && MathJax.startup && MathJax.startup.promise",
                               timeout=120_000)
        page.evaluate("MathJax.startup.promise")
        page.wait_for_timeout(2000)
        print(f"MathJax finished in {time.time() - t0:.0f} s")
        page.pdf(path=str(PDF), format="A4", print_background=True,
                 display_header_footer=True, header_template="<div></div>",
                 footer_template=FOOTER,
                 margin={"top": "16mm", "bottom": "18mm", "left": "15mm", "right": "15mm"})
        browser.close()
    print(f"PDF written to {PDF} ({PDF.stat().st_size / 1e6:.1f} MB)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--no-build", action="store_true", help="reuse an existing singlehtml build")
    args = parser.parse_args()
    if not args.no_build:
        build_singlehtml()
    print_pdf()


if __name__ == "__main__":
    main()
