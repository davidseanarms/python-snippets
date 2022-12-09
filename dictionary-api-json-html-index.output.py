import requests
import json
import html

# Ask for a word input
word = input('Please enter a word: ')

# Use the https://api.dictionaryapi.dev/api/v2/ API to look up the input word
url = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + word
response = requests.get(url)

# Output the JSON result from the API
data = response.json()
json_output = json.dumps(data, indent=2)
print(json_output)

# Convert the JSON output to HTML5
html_output = html.escape(json.dumps(data))

# Save HTML5 output as index.html
with open('index.html', 'w') as f:
    f.write(html_output)

# Print end of script confirmation
print('Script finished! HTML file saved as index.html')
