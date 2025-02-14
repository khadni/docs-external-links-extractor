import pandas as pd
import re
from datetime import datetime
import argparse
import logging
import sys

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def parse_file(file_path):
    """
    Parse the log file and extract data into a DataFrame.

    Parameters:
        file_path (str): The path to the log file.

    Returns:
        pd.DataFrame: A DataFrame containing the extracted data.
    """
    data = []

    # Compile regex pattern once
    pattern = re.compile(r"-\s\((\d+:\d+)\).*=>\s(https?://[^\s]+)\s\(([^)]+)\)")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            current_page = None

            # Iterate through each line
            for line in file:
                line = line.strip()
                # Check if the line is a URL
                if line.startswith("http://localhost:"):
                    current_page = line
                # Otherwise, it might be a link entry
                else:
                    if current_page:
                        match = pattern.search(line)
                        if match:
                            position = match.group(1)
                            link = match.group(2)
                            reason = match.group(3)
                            data.append([current_page, position, link, reason])
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"An error occurred while parsing the file: {e}")
        sys.exit(1)
    
    # Create a DataFrame from the data
    return pd.DataFrame(data, columns=["Page", "Position", "Link", "Reason"])

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Extract link data from log file.')
    parser.add_argument('--input', '-i', required=True, help='Path to the input log file.')
    parser.add_argument('--output', '-o', help='Path to the output CSV file.')

    args = parser.parse_args()

    file_path = args.input
    csv_file_path = args.output

    # Parse the file and create a DataFrame
    df = parse_file(file_path)

    # Set default output file path if not provided
    if not csv_file_path:
        current_date = datetime.now().strftime("%Y%m%d")
        csv_file_path = f"output_{current_date}.csv"

    # Save the DataFrame to a CSV file
    try:
        df.to_csv(csv_file_path, index=False)
        logging.info(f"Data saved to {csv_file_path}")
    except Exception as e:
        logging.error(f"An error occurred while saving the CSV file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()