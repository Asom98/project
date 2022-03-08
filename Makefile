#!/usr/bin/env make

# Change this to be your variant of the python command
PYTHON ?= python # python3 py

# Print out colored action message
MESSAGE = printf "\033[32;01m---> $(1)\033[0m\n"

# To make targets in each directory under the src/
define FOREACH
    for DIR in src/*; do \
        $(MAKE) -C $$DIR $(1); \
    done
endef

all:


# ---------------------------------------------------------
# Setup a venv and install packages.
#
version:
	@printf "Currently using executable: $(PYTHON)\n"
	which $(PYTHON)
	$(PYTHON) --version

venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv
	@printf "Now activate the Python virtual environment.\n"
	@printf "On Unix and Mac, do:\n"
	@printf ". .venv/bin/activate\n"
	@printf "On Windows (bash terminal), do:\n"
	@printf ". .venv/Scripts/activate\n"
	@printf "Type 'deactivate' to deactivate.\n"

install:
	$(PYTHON) -m pip install -r requirements.txt

installed:
	$(PYTHON) -m pip list


# ---------------------------------------------------------
# Cleanup generated and installed files.
#
clean:
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov

clean-doc:
	rm -rf doc

clean-src:
	$(call FOREACH,clean)

clean-all: clean clean-doc clean-src
	rm -rf .venv


# ---------------------------------------------------------
# Test all the code at once.
#
pylint:
	$(call FOREACH,pylint)

flake8:
	$(call FOREACH,flake8)

lint: flake8 pylint

test:
	$(call FOREACH,test)