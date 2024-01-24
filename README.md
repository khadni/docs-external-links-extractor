# CLL Documentation External Links Checker

This project includes tools and scripts to check external links in the documentation repository. It automates identifying broken or problematic links and outputs the results in a convenient CSV format for further analysis.

## Prerequisites

- **Python**: Required to run the Python script for processing link check results. [Download Python](https://www.python.org/downloads/).
- **Pandas Library**: Python library for data manipulation. Install it via pip using `pip install pandas`.
- **Node.js and npm**: Required for running the `linkcheck-external` script. [Download Node.js and npm](https://nodejs.org/en/download/).

## Generating the log file

### Cloning the Documentation Repository

1.  Clone the documentation repository to your local machine:

        git clone https://github.com/smartcontractkit/documentation

2.  Navigate to the cloned directory:

        cd documentation

### Running the Link Checker

1.  In the repository directory, install the required Node.js dependencies:

        npm install

2.  Run the `linkcheck-external` script to check external links:

        npm run linkcheck-external

This script generates a log file `link-checker.log` in the `temp` folder with the link check results.

## Reformatting the log file in a convenient CSV format

### Cloning the Extractor Repository

1.  Clone the Extractor repository to your local machine:

        git clone https://github.com/khadni/docs-external-links-extractor

2.  Navigate to the cloned directory:

        cd docs-external-links-extractor

### Processing the Link Checker Output

1.  Copy the `link-checker.log` log file from the `documentation` folder and paste it into the `docs-external-links-extractor` folder.

1.  In your terminal, run the Python script to parse the log file and generate a CSV file with link errors shown in a convenient format:

        python Extractor.py

The script creates a new CSV file `output_[YYYYMMDD].csv`.

## Importing results into Google Sheets

1. Open Google Sheets and create a new spreadsheet.

1. Go to `File > Import > Upload` and select the generated CSV file.

1. Click on `Import data`.
