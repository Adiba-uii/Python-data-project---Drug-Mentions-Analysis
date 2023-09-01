import unittest
import sys
#sys.path.append("../workflow")
from workflow.data_utilities import load_from_json, save_to_json, process_data
from main import extract_drugs, extract_publications, extract_trials, extract_journals
from workflow.data_checking import check_csv_headers, check_json_structure 


class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        # Set up test data
        self.drugs = extract_drugs('tests/data_test/drugs.csv')
        self.pubmed_publications = extract_publications('tests/data_test/pubmed.json')
        self.clinical_trials = extract_trials('tests/data_test/clinical_trials.csv')
        self.journals = extract_journals('tests/data_test/pubmed.csv')

    def test_process_data(self):
        # Test the process_data function
        data = process_data(self.drugs, self.pubmed_publications, self.clinical_trials, self.journals)
        self.assertTrue(isinstance(data, dict))
        self.assertTrue(len(data) > 0)

    def test_save_and_load_json(self):
        # Test saving and loading JSON data
        test_data = {'example_key': 'example_value'}
        save_to_json(test_data, 'tests/test_output/test_data.json')
        loaded_data = load_from_json('tests/test_output/test_data.json')
        self.assertEqual(test_data, loaded_data)

    def test_check_csv_headers(self):
        # Test the check_csv_headers function
        try:
            check_csv_headers('tests/data_test/drugs.csv', ['atccode', 'drug']) 
        except ValueError as e:
            self.fail(f"check_csv_headers raised an exception: {e}")

    def test_check_json_structure(self):
        # Test the check_json_structure function
        try:
            check_json_structure('tests/data_test/pubmed.json', ['id', 'title', 'journal', 'date']) 
        except ValueError as e:
            self.fail(f"check_json_structure raised an exception: {e}")


if __name__ == '__main__':
    unittest.main()
