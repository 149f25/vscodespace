#!/usr/bin/env bash
python -m venv .venv
source .venv/bin/activate
pip install ruff pytest-cov pysyllables
