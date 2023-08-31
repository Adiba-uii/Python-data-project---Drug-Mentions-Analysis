import csv
import json
from constants import DRUGS_CSV_HEADERS, PUBMED_JSON_KEYS, CLINICAL_TRIALS_CSV_HEADERS, PUBMED_CSV_HEADERS
from workflow.data_checking import check_csv_headers, check_json_structure

# Function to extract drugs data
def extract_drugs(file_path):
    check_csv_headers(file_path, DRUGS_CSV_HEADERS)
    drugs = {}
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            drugs[row['atccode']] = row['drug']
    return drugs

# Function to extract publications data from JSON
def extract_publications(file_path):
    check_json_structure(file_path, PUBMED_JSON_KEYS)
    with open(file_path, 'r') as jsonfile:
        data = json.load(jsonfile)
    return data

# Function to extract clinical trials data
def extract_trials(file_path):
    check_csv_headers(file_path, CLINICAL_TRIALS_CSV_HEADERS)
    trials = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            trials.append(row)
    return trials

# Function to extract journal data
def extract_journals(file_path):
    check_csv_headers(file_path, PUBMED_CSV_HEADERS)
    journals = set()
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            journals.add(row['journal'])
    return list(journals)
