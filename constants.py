# Define expected headers for CSV files
PUBMED_JSON_KEYS = ['id', 'title', 'journal', 'date']
CLINICAL_TRIALS_CSV_HEADERS = ['id', 'scientific_title', 'journal', 'date']
PUBMED_CSV_HEADERS = ['id', 'journal', 'title', 'date']
DRUGS_CSV_HEADERS = ['atccode', 'drug']

# Define expected paths for CSV / Json files
PUBMED_PATH_JSON = "data/pubmed.json"
CLINICAL_PATH = "data/clinical_trials.csv"
DRUGS_PATH = "data/drugs.csv"
PUBMED_CSV_PATH = "data/pubmed.csv"
OUTPUT_JSON_FILE = "output/output.json"
