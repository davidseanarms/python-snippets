import csv
import xlrd ## xlrd is a library for reading data and formatting information from Excel files in the historical .xls format.

#prompt user to enter the excel spreadsheet
filename = input('Enter the filename of the spreadsheet: ')

#open the excel spreadsheet and create a csv file
wb = xlrd.open_workbook(filename)
sh = wb.sheet_by_index(0)
csv_filename = 'country.csv'
csv_file = open(csv_filename, 'w')
csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

#write the contents of the excel sheet to the csv file
for row_num in range(sh.nrows):
csv_writer.writerow(sh.row_values(row_num))

#close the csv file
csv_file.close()

#open and read the csv file
csv_file = open(csv_filename, 'r')
csv_reader = csv.reader(csv_file)

#create a dictionary with the contents of the csv file
country_dict = {}

for row in csv_reader:
country_dict[row[0]] = row[1]

#close the csv file
csv_file.close()

#lookup function to lookup the country code prefix
def lookup(country):
return country_dict[country]

#prompt user to enter a country
country = input('Enter a country: ')

#call the lookup function to get the country code prefix
country_prefix = lookup(country)

#print the country code prefix
print('The country code prefix for', country, 'is', country_prefix)
