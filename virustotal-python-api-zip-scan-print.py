# Import virustotal-python library
import virustotal_python

# Get user input for file to scan
file_to_scan = input("Enter the path of the file to scan: ")

# Initiate the virustotal-python library
vt = virustotal_python.VirusTotal("<Your API Key>")

# Upload the file to VirusTotal
uploaded_file = vt.scan_file(file_to_scan)

# Get the scan results
results = uploaded_file.get_results()

# Print the scan results
if results:
    print(results)
else:
    print("No scan results found")
