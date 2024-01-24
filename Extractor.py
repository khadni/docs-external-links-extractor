import pandas as pd
import re
from datetime import datetime

# Function to parse the text data from the log.txt file
def parse_file(file_path):

    data = []

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Initialize a variable to store the current page URL
    current_page = None

    # Iterate through each line
    for line in lines:
        # Check if the line is a URL
        if line.startswith("http://localhost:"):
            current_page = line.strip()
        # Otherwise, it might be a link entry
        else:
            # Regex pattern to extract position, link, and reason
            match = re.search(r"-\s\((\d+:\d+)\).*=>\s(https?://[^\s]+)\s\(([^)]+)\)", line)
            if match and current_page:
                position = match.group(1)
                link = match.group(2)
                reason = match.group(3)
                data.append([current_page, position, link, reason])

    # Create a DataFrame from the data
    return pd.DataFrame(data, columns=["Page", "Position", "Link", "Reason"])

file_path = "./link-checker.log"

# Parse the file and create a DataFrame
df = parse_file(file_path)

# Get the current date in YYYYMMDD format
current_date = datetime.now().strftime("%Y%m%d")

# Specify the path for the CSV file with the current date
csv_file_path = f"output_{current_date}.csv"

# Save the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

print(f"Data saved to {csv_file_path}")
