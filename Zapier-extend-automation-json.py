# This script is used to extend Zapier automations and integrations
import json
import requests

# Retrieve data from our source
data = requests.get('http://example.com/data')
data_json = json.loads(data.content)

# Format the data for Zapier
formatted_data = {
    'name': data_json['name'],
    'email': data_json['email'],
    'phone': data_json['phone'],
    'address': data_json['address']
}

# Send the formatted data to Zapier
zapier_url = 'https://hooks.zapier.com/hooks/catch/<zapier_id>/<hook_id>'
requests.post(zapier_url, data=formatted_data)
