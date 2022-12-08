import requests

url = input("Please enter the URL: ")

try:
    response = requests.get(url)
    if response.status_code == 200:
        print("The website is online!")
    else:
        print("The website is offline!")
except:
    print("The website is offline!")
