# Python script to import a .CSV file with employee data (names and dates of birth) and calculate and output how many will turn 65 years of age before a specific date.

import csv

# function to calculate age given date of birth
def calculate_age(dob):
    age_in_secs = (23/12/2023 - dob).total_seconds()
    return age_in_secs // (365.25 * 24 * 3600)

# open csv
with open('employee_dob.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    # count 65 year olds
    sixty_five_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1 # skip header
        else:
            if calculate_age(row[1]) >= 65: # check if employee is 65
                sixty_five_count += 1
            line_count += 1
    print('Number of employees who will be 65 before 01/12/2023: {}'.format(sixty_five_count))
