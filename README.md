# CSV Cleaner CLI

A reusable Python CLI for normalizing, inspecting, and deduplicating tabular CSV data.

## Features

- trims surrounding whitespace from headers and values;
- rejects header collisions introduced by normalization;
- detects missing values without assuming every cell is a string;
- finds and removes duplicate rows deterministically;
- tolerates malformed rows and creates output directories;
- logs a concise cleaning summary.

## Usage

```bash
python -m src.main data/input.csv data/cleaned.csv
```

## Tests

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

## Stack

Python 3.11+, argparse, csv, logging, pytest. Runtime dependencies: none.
