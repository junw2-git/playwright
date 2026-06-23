import os
import json
import csv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_json(file_path):
    file_path = os.path.join(BASE_DIR, "data", file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_csv(file_path):
    file_path = os.path.join(BASE_DIR, "data", file_path)
    data = []
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data
