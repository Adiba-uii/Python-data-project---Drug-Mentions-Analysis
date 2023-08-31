# Import necessary functions and classes from the modules
from workflow.data_processing import extract_drugs, extract_publications, extract_trials, extract_journals
from workflow.data_utilities import process_data, save_to_json, load_from_json
from collections import Counter
from constants import CLINICAL_PATH, PUBMED_PATH_JSON, DRUGS_PATH, PUBMED_CSV_PATH, OUTPUT_JSON_FILE


# Function to find the journal with the most mentions in the data
def find_journal_with_most_mentions(data):
    journals_mentions = Counter()
    most_mentioned_journal = ""
    most_mentions = 0
    most_mentioned_drug = ""

    # Iterate through drugs and their mentions in the data
    for drug, mentions in data.items():
        for mention in mentions:
            journal = mention['journal']
            # Count the mentions of each journal
            journals_mentions[journal] += 1
    
    # Update the most mentioned journal and its associated drug
            if journals_mentions[journal] > most_mentions:
                most_mentions = journals_mentions[journal]
                most_mentioned_journal = journal
                most_mentioned_drug = drug
    return most_mentioned_journal, most_mentions, most_mentioned_drug


# Main entry point of the script
def main():
    # Extract data from different sources
    drugs = extract_drugs(DRUGS_PATH)
    pubmed_publications = extract_publications(PUBMED_PATH_JSON)
    clinical_trials = extract_trials(CLINICAL_PATH)
    journals = extract_journals(PUBMED_CSV_PATH)

    # Process and transform the extracted data
    data = process_data(drugs, pubmed_publications, clinical_trials, journals)

    # Save the processed data as JSON
    save_to_json(data, OUTPUT_JSON_FILE)

    # Load the saved data from JSON
    output_data = load_from_json(OUTPUT_JSON_FILE)

    # Find the journal with the most mentions and print the result
    most_mentioned_journal, mentions, drug = find_journal_with_most_mentions(output_data)
    print(f"The journal with the most mentions is '{most_mentioned_journal}' with {mentions} mentions for the drug :{drug}.")

# Entry point of the script: run the main function if this script is executed directly
if __name__ == "__main__":
    main()
