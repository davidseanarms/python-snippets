# import libraries
import requests
import json

# ask user to enter eircode
eircode = input("Enter an Irish eircode: ")

# make a get request
url = "https://api.eircode.ie/v2/lookup/" + eircode
response = requests.get(url)

# check if eircode is valid
if response.status_code == 200:
    # parse response
    data = response.json()
    # get the postal code
    postal_code = data["postal_code"]
    # print the result
    print("The postal code for this eircode is " + postal_code + ".")
else:
    print("The eircode entered is not valid.")
