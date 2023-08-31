# Data Processing Project - Drug Mentions Analysis

Welcome to the Data Processing Project for analyzing drug mentions in scientific publications and journals. This project demonstrates how to extract, process, and analyze data related to drug mentions using Python.

## Project Overview

This project aims to process data from various sources, including CSV and JSON files, to identify drug mentions in scientific publications and journals. The goal is to generate a data pipeline that produces a JSON file representing the relationships between drugs and their mentions.

## Project Structure

The project is organized as follows:

project_root/
├── data/
│ ├── drugs.csv
│ ├── pubmed.csv
│ ├── pubmed.json
│ ├── clinical_trials.csv
├── workflow/
| ├── __init__.py
│ ├── data_processing.py
│ ├── data_utilities.py
│ ├── data_checking.py
├── output/
│ ├── output.json
├── README.md
├── main.py
├── constants.py


- `data/`: Contains the input data files.
- `workflow/`: Includes modules for data processing and utilities.
- `main.py`: The main script that orchestrates the data processing pipeline.
- `output/`: Directory to store the generated output JSON file.
- `README.md`: This file, providing project information and instructions.
- `constants.py` file contains important constants used throughout the project. These constants help maintain consistency and readability in the code.

## Getting Started

1. Populate the `data/` directory with the input data files: `drugs.csv`, `pubmed.csv`, `pubmed.json`, and `clinical_trials.csv`.
2. Run the data processing pipeline using `python main.py`.

## Functionality

- The `workflow/` folder contains data processing modules such as `data_processing.py` and `data_utilities.py`.
- `main.py` is the entry point of the project. It extracts data, processes it, and generates the output JSON file.
- The `output/` folder contains the output.json` file that represents the relationships between drugs and their mentions.

## Future Enhancements

- Optimize processing for large datasets.
- Add more advanced data quality checks.
- Improve error handling and reporting.
- Enhance documentation and testing.


