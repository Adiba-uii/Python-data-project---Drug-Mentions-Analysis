import csv
import json

# Function to check CSV file headers
def check_csv_headers(file_path, expected_headers):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        # Check if the headers are the same, regardless of order
        if set(headers) != set(expected_headers):
            raise ValueError(f"Unexpected headers in '{file_path}'. Expected: {expected_headers}, Found: {headers}")

# Function to check JSON file structure
def check_json_structure(file_path, expected_keys):
    with open(file_path, 'r') as jsonfile:
        data = json.load(jsonfile)
        for item in data:
            missing_keys = [key for key in expected_keys if key not in item]
            if missing_keys:
                raise ValueError(f"Missing keys in '{file_path}' JSON item. Expected: {expected_keys}, Missing: {missing_keys}")