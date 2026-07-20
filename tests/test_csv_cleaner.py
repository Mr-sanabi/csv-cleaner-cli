import csv

import pytest

from src.cleaner import clean_rows, find_duplicate_rows, find_missing_values
from src.storage import read_csv, save_csv


def test_clean_rows_normalizes_headers_values_and_duplicates():
    rows = [
        {" Full Name ": " Alice ", "E mail": " alice@example.com "},
        {" Full Name ": " Alice ", "E mail": " alice@example.com "},
    ]

    cleaned = clean_rows(rows)

    assert cleaned[0] == {"full_name": "Alice", "e_mail": "alice@example.com"}
    assert find_duplicate_rows(cleaned) == [{"row": 2}]


def test_normalized_header_collision_is_rejected():
    with pytest.raises(ValueError, match="collision"):
        clean_rows([{"First Name": "A", "first_name": "B"}])


def test_missing_values_and_nested_output_directory(tmp_path):
    source = tmp_path / "source.csv"
    output = tmp_path / "nested" / "clean.csv"
    source.write_text("name,email\nAlice,\n", encoding="utf-8")

    rows = read_csv(source)
    assert find_missing_values(rows) == [{"row": 1, "column": "email"}]

    save_csv(output, rows)
    with output.open(encoding="utf-8", newline="") as file:
        assert list(csv.DictReader(file)) == rows
