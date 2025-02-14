# CL Documentation External Links Checker

This project includes tools and scripts to check external links in the documentation repository. It automates identifying broken or problematic links and outputs the results in a convenient CSV format for further analysis.

## Prerequisites

- **Python**: Required to run the Python script for processing link check results. [Download Python](https://www.python.org/downloads/).
- **Node.js and npm**: Required for running the `linkcheck-external` script. [Download Node.js and npm](https://nodejs.org/en/download/).

> **Note:** The Python dependencies (e.g., Pandas) will be installed within a virtual environment.

## Generating the Log File

### Cloning the Documentation Repository

1. Clone the documentation repository to your local machine:

   ```bash
   git clone https://github.com/smartcontractkit/documentation
   ```

2. Navigate to the cloned directory:

   ```bash
   cd documentation
   ```

### Running the Link Checker

1. In the repository directory, install the required dependencies:

   ```bash
   npm install
   ```

2. Run the `linkcheck-external` script to check external links:

   ```bash
   npm run linkcheck-external
   ```

   This script generates a log file named `link-checker.log` in the `temp` folder with the link check results.

## Reformatting the Log File in a Convenient CSV Format

### Cloning the Extractor Repository

1. Clone the Extractor repository to your local machine:

   ```bash
   git clone https://github.com/khadni/docs-external-links-extractor
   ```

2. Navigate to the cloned directory:

   ```bash
   cd docs-external-links-extractor
   ```

### Setting Up the Python Virtual Environment

It is recommended to use a Python virtual environment to manage project dependencies.

1. **Create the Virtual Environment:**

   ```bash
   python3 -m venv venv
   ```

2. **Activate the Virtual Environment:**

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

3. **Install Required Dependencies:**

   With the virtual environment activated, install the Pandas library:

   ```bash
   pip install pandas
   ```

### Processing the Link Checker Output

1. Copy the `link-checker.log` file from the `documentation/temp` folder and paste it into the `docs-external-links-extractor` folder.

2. With the virtual environment still activated, run the Python script to process the log file:

   ```bash
   python Extractor.py --input link-checker.log
   ```

   This script will:

   - Parse the log file to extract information about problematic links.
   - Generate a CSV file named `output_[YYYYMMDD].csv` containing:
     - The page URL where the link was found.
     - The position of the link in the document.
     - The problematic link URL.
     - The reason for the link failure.

   **Optional:** Specify a custom output file by adding the `--output` (or `-o`) argument:

   ```bash
   python Extractor.py --input link-checker.log --output problematic_links.csv
   ```

   If the `--output` argument is not provided, the CSV file will be saved in your current directory with today's date in the format `output_YYYYMMDD.csv` (for example, `output_20231115.csv`).

## Importing Results into Google Sheets

1. Open [Google Sheets](https://sheets.google.com) in your browser and create a new spreadsheet.

2. Import the CSV file:

   - Click `File` in the top menu.
   - Select `Import`.
   - Choose `Upload` from the options.
   - Select the `output_[YYYYMMDD].csv` file from your computer.

3. In the Import dialog:
   - Choose "Replace current sheet" as the import location.
   - Select "Comma" as the separator type.
   - Click `Import data` to complete the import.

The spreadsheet will now display your link checker results in an organized table format.
