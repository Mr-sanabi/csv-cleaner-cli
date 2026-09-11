# CSV Cleaner CLI

A Python 3.11+ command-line tool that trims CSV headers and values, checks missing values, and removes duplicate rows.
No runtime dependencies.

## Run

```bash
python -m src.main data/input.csv data/cleaned.csv
```

Headers that collide after trimming are rejected. Missing output directories are created automatically. This is basic cleanup, not domain-specific data validation.

## Tests

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```
