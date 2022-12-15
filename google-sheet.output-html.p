# This program takes a link to a Google Sheet and converts it into an HTML file.
# Import libraries
import pandas as pd
import requests

sheet_url = input("Please provide the link to the Google Sheet you want to convert to HTML: ")

sheet_data = pd.read_csv(sheet_url)

f = open("data.html","w+")

for i in range(len(sheet_data.columns)):
    column_name = sheet_data.columns[i]
    heading_type = column_name[:2]
    # Check if column name starts with "H1", "H2", "H3", "H4", "H5", "H6" or "p"
    if heading_type in ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'p']:
        for j in range(len(sheet_data)):
            f.write(f"<{heading_type}>{str(sheet_data.iloc[j,i])}</{heading_type}>\n")

f.close()

def write_html(path):
    with open(path, "w") as f:
        f.write(f.read())

path = input("Please provide the path where you want to save the HTML file: ")

write_html(path)

print("HTML file successfully written to: ", path)
