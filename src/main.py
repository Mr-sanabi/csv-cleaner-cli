import logging
import argparse
from src.storage import read_csv, save_csv
from src.cleaner import clean_rows, find_missing_values, find_duplicate_rows, remove_duplicate_rows
from src.logger_config import setup_logging


def parse_args():
    parser = argparse.ArgumentParser(
        description="Normalize, inspect, and deduplicate CSV rows."
    )
    parser.add_argument("input_file", help="Path to the source CSV file")
    parser.add_argument("output_file", help="Path for the cleaned CSV file")
    return parser.parse_args()


def main():
    setup_logging()
    args = parse_args()
    logging.info("CSV Cleaner started")
    try:
        data = read_csv(args.input_file)
    except FileNotFoundError:
        logging.error(f"Input file not found: {args.input_file}")
        return 
    if not data:
        logging.error(f"CSV file is empty: {args.input_file}")
        return 
    cleaned_rows = clean_rows(data)
    missing_values = find_missing_values(cleaned_rows)
    duplicate_rows = find_duplicate_rows(cleaned_rows)
    unique_rows = remove_duplicate_rows(cleaned_rows)
    save_csv(args.output_file, unique_rows)

    summary = (
        "Cleaning summary\n"
        f"Rows loaded: {len(data)}\n"
        f"Rows after cleaning: {len(cleaned_rows)}\n"
        f"Missing values found: {len(missing_values)}\n"
        f"Duplicate rows found: {len(duplicate_rows)}\n"
        f"Rows saved: {len(unique_rows)}\n"
        f"Output file: {args.output_file}"
    )

    logging.info(summary)

if __name__ == "__main__":
    main()
