# Refactored Code
import requests
from bs4 import BeautifulSoup

# Ask for a URL
url = input("Please enter a URL: ")

# Scrape URL for text
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
text = soup.get_text()

# Output the sentences containing questions
questions = [sentence.strip() for sentence in text.split('.') if '?' in sentence]
for question in questions:
    print(question)
