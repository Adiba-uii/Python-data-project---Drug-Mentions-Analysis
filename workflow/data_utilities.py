import json

# Process the extracted data to find mentions of drugs in publications and trials
def process_data(drugs, pubmed_data, clinical_trials, journals):
    data = {}

    # Iterate through each drug and its mentions
    for drug_id, drug_name in drugs.items():
        drug_mentions = []
        
        # Check drug mentions in PubMed data
        for publication in pubmed_data:
            if drug_name.lower() in publication['title'].lower():
                drug_mentions.append({
                    'type': 'PubMed',
                    'id': publication['id'],
                    'journal': publication['journal'],
                    'date': publication['date']
                })
        
        # Check drug mentions in clinical trials data
        for trial in clinical_trials:
            if drug_name.lower() in trial['scientific_title'].lower():
                drug_mentions.append({
                    'type': 'ClinicalTrial',
                    'id': trial['id'],
                    'journal': trial['journal'],
                    'date': trial['date']
                })
        
        # Store the drug mentions in the data dictionary
        data[drug_name] = drug_mentions

    return data

# Save processed data to a JSON file
def save_to_json(data, output_file):
    with open(output_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

# Load data from a JSON file
def load_from_json(file_path):
    with open(file_path, 'r') as jsonfile:
        data = json.load(jsonfile)
    return data
