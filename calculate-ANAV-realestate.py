# **Adjusted Net Asset Value (`ANAV`)** is a measure of the fair market value of a parcel of land.
# It is calculated by taking the **estimated value of the land**, **subtracting any outstanding debt** or other liabilities associated with the land, and **adding any estimated value of potential future income** (or profit) that can be generated from the land.
# For example, let's say you have a parcel of land valued at **$200,000**.
# It has an **outstanding mortgage of $80,000** and you estimate that you can **generate $20,000** in **rental income** from the land.
# The **`ANAV`** for this parcel would be calculated as follows: $200,000 - $80,000 + $20,000 = $140,000

import pandas as pd 
import numpy as np 

# Read Google Sheets Data
url = "https://docs.google.com/spreadsheets/d/1DV6fMd6KU6qX9Ywdox0f2vU6yOlyjKF0bG8fBVpTlEg/edit#gid=0"
data = pd.read_excel(url, sheet_name="Sheet1") 

# Calculate ANAV 
data["ANAV"] = data['Estimated Value of Land'] - data["Outstanding Debt or Other Liabilities"] + data["Estimated Value of Potential Future Income"]

# Output to DataFrame
output = data[["Property Address", "ANAV"]] 
print(output)
