"""Build the finished edition and put publishable HTML in docs/."""
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / '.site-build'
DOCS = ROOT / 'docs'

subprocess.run([sys.executable, str(ROOT / 'scripts/build_equation_previews.py')], cwd=ROOT, check=True)
subprocess.run([sys.executable, '-c', 'from jupyter_book.cli.main import main; main()', 'build', str(ROOT / 'book'), '--all', '--path-output', str(BUILD)], cwd=ROOT, check=True)
html = BUILD / '_build' / 'html'
if not (html / 'index.html').is_file():
    raise RuntimeError('HTML build did not produce index.html')
if DOCS.exists():
    shutil.rmtree(DOCS)
shutil.copytree(html, DOCS)
(DOCS / '.nojekyll').touch()
shutil.rmtree(BUILD)
print(f'Publishable HTML: {DOCS / "index.html"}')
