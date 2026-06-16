def normalize_column_name(column_name: str) -> str:
    return (
        str(column_name)
        .strip()
        .lower()
        .replace(" ", "_")
    )

def normalize_row_keys(row):
    new_row = {}
    for key, value in row.items():
        clean_key = normalize_column_name(key)
        new_row[clean_key] = value

    return new_row

def clean_value(value):
    if isinstance(value, str):
        return value.strip()
    else:
        return value
    
def clean_row_values(row):
    clean_row = {}
    for key, value in row.items():
        clean_row[key] = clean_value(value)
    
    return clean_row

def clean_rows(rows):
    cleaned_rows = []
    for row in rows:
        normalized_row = normalize_row_keys(row)
        cleaned_row = clean_row_values(normalized_row)
        cleaned_rows.append(cleaned_row)
    return cleaned_rows

def find_missing_values(rows):
    missing_values = []

    for row_number, row in enumerate(rows, start=1):
        for column, value in row.items():
            if value is None or value.strip() == "":
                missing_values.append({
                    "row": row_number,
                    "column": column
                })

    return missing_values

def find_duplicate_rows(rows):
    seen = set()
    duplicates = []

    for row_number, row in enumerate(rows, start=1):
        row_signature = tuple(row.items())
        if row_signature in seen:
            duplicates.append({
                "row": row_number
            })
        else:
            seen.add(row_signature)

    return duplicates

def remove_duplicate_rows(rows):
    seen = set()
    unique_rows = []

    for row in rows:
        row_signature = tuple(row.items())
    

        if row_signature not in seen:
            seen.add(row_signature)
            unique_rows.append(row)

    return unique_rows