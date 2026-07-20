import csv 
from pathlib import Path

def read_csv(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [row for row in reader if None not in row]

def save_csv(filename, data):
    if not data:
        return
    
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = data[0].keys()
    
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        
        writer.writeheader()
        writer.writerows(data)
