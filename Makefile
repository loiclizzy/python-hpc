
IPYNBDIR := ipynb

IPYNBFILES := $(shell find $(IPYNBDIR) -name '*.ipynb' | grep -v ipynb_checkpoints)

IPYNBPRES = $(addsuffix .slides.html, $(basename $(IPYNBFILES)))

# TPL_FILE = ipynb/slides_reveal_wide.tpl
TPL_FILE = ipynb/slides_reveal.tpl

define STR_HELP
This makefile can be used for

help: print this help.

lab: run jupyter-lab.

presentations: build the html presentations.

serve: launch a small server to display the notebooks with reveal.js

endef

export STR_HELP

.PHONY: help lab serve presentations ipynb/index.rst

help:
	@echo "$$STR_HELP"

clean:
	rm -f ipynb/*.slides.html
	rm -f ipynb/index.html
	rm -rf ipynb/tmp

lab:
	jupyter-lab

ipynb/index.rst:
	python ipynb/make_index.py

ipynb/index.html: ipynb/index.rst
	cd $(IPYNBDIR) && rst2html5 index.rst > index.html

%.slides.html: %.ipynb $(TPL_FILE)
	jupyter-nbconvert $< --reveal-prefix='./reveal.js' --to slides --template $(TPL_FILE)

presentations: $(IPYNBPRES) ipynb/index.html

serve: $(IPYNBPRES) ipynb/index.html
	cd $(IPYNBDIR) && python3 -m http.server
