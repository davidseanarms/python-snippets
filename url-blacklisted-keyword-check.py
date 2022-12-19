# This script is intended to allow a user to enter a URL and check to see if any of the words on a blacklist appear in the URL. It retrieves the blacklist from a URL, splits it into individual words, and then checks the user-entered URL for any of those words. If any of the words on the blacklist appear in the URL, they are printed out. Otherwise, the user is notified that no blacklisted words appear in the URL.

import requests

# get the blacklist from the URL
url = 'https://gist.githubusercontent.com/splorp/1385930/raw/8e12a46eee708b31a0d16a55ae49cd83b77e2aca/wp-comment-blacklist-keywords.txt'
response = requests.get(url)
blacklist = response.text.split('\n')

# get user input of URL
user_url = input('Enter a URL to read and parse the text: ')

# check the presence of blacklisted words in the URL
blacklisted_words = [word for word in blacklist if word in user_url]

# print the output
if blacklisted_words:
	print('The following blacklisted words appear in the URL:')
	for word in blacklisted_words:
		print(word)
else:
	print('No blacklisted words appear in the URL.')
