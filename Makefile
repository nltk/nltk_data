PYTHON = python3
BASEURL = https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages

pkg_index:
	$(PYTHON) tools/build_collections.py .
	$(PYTHON) tools/build_pkg_index.py . $(BASEURL) index.xml
	git add collections
	git add index.xml
	git commit -m "updated data index"

grammars:
	git commit -m "updated grammar files" packages/grammars

