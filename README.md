# CSV Cleaner CLI

CSV Cleaner CLI is a small Python command-line tool that reads a messy CSV file, cleans the data, and saves a cleaned version as a new CSV file.

## Features

* Reads CSV files using Python's standard `csv` module.
* Normalizes column names.
* Trims extra spaces from values.
* Detects missing values.
* Detects duplicate rows.
* Removes duplicate rows.
* Saves cleaned data to a new CSV file.
* Prints a cleaning summary in the console.

## Tech Stack

* Python
* csv
* argparse
* logging

## How to Run

This project currently uses only Python standard library modules, so no external dependencies are required.

Run the cleaner:

```bash
python src/main.py data/input_sample.csv data/output_cleaned.csv
```

Arguments:

* `input_file` — path to the source CSV file.
* `output_file` — path where the cleaned CSV will be saved.

## Example

Input CSV may contain messy headers, extra spaces, missing values, and duplicate rows.

Example output summary:

```text
Cleaning summary
Rows loaded: 5
Rows after cleaning: 5
Missing values found: 1
Duplicate rows found: 1
Rows saved: 4
Output file: data/output_cleaned.csv
```

## Current Status

MVP completed and published.

The project can read a CSV file from a CLI argument, clean headers and values, detect missing values, detect and remove duplicate rows, save cleaned data to a new CSV file, and generate a logging-based cleaning summary.

## Do Not Commit

Generated output files should not be committed:

```text
data/output_cleaned.csv
log.txt
```
