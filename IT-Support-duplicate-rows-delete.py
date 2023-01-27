#!/usr/bin/env python

import csv

# initialize variables
duplicates_found = 0
rows_to_delete = []

# open csv file
with open('data.csv', 'r+') as data_file:
    reader = csv.reader(data_file)

    # iterate through csv file
    for row in reader:
        # check for duplicate rows
        if row in reader:
            duplicates_found += 1
            
            # prompt user to delete one of the duplicates
            print("Duplicate row found: ", row)
            delete_row = input("Do you want to delete one of the duplicates? (Y/N): ")
            
            # delete row if user selects 'Y'
            if delete_row.lower() == 'y':
                rows_to_delete.append(row)
                
    # iterate through csv file
    data_file.seek(0)
    for line in data_file:
        for row in rows_to_delete:
            if row in line:
                data_file.write("")
                
# output number of duplicate rows found
print("Number of duplicate rows found: ", duplicates_found)
