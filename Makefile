# Common tasks for the Biomedical Signal Processing book.
# Run `make help` to list them.

BOOK := book
PY   := python

.PHONY: help html pdf execute data serve clean

help:
	@echo "make html     build the publishable website into docs/"
	@echo "make pdf      build the PDF into book/_build/pdf"
	@echo "make execute  re-run every notebook and store fresh outputs"
	@echo "make data     download the PhysioNet records into book/data"
	@echo "make serve    preview the website at http://localhost:8000"
	@echo "make clean    remove build artifacts"

html:
	$(PY) scripts/build_site.py

pdf:
	$(PY) scripts/build_pdf.py

execute:
	jupyter nbconvert --to notebook --execute --inplace \
		--ExecutePreprocessor.timeout=900 $(BOOK)/ch*/*.ipynb $(BOOK)/appendix/*.ipynb

data:
	$(PY) scripts/download_data.py

serve:
	$(PY) -m http.server 8000 --directory docs

clean:
	jupyter-book clean $(BOOK)
