#import libraries
import os
import googleapiclient.discovery

#API key
API_KEY = ""

# Get the video ID
# Ask user for URL
url = input("Please enter the URL of the YouTube video: ")

# Extract the video ID
video_id = url.split("=")[1]

# Create the API service object
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

# Get the list of closed captions from the video
caption_list = youtube.captions().list(
    part="snippet",
    videoId=video_id
).execute()

# Get the closed caption ID
caption_id = caption_list["items"][0]["id"]["videoId"]

# Get the closed caption
caption = youtube.captions().download(
    id=caption_id
).execute()

# Save the closed caption as a text file
file_name = os.path.splitext(os.path.basename(url))[0]
with open(f"{file_name}.txt", "wb") as f:
    f.write(caption)

print(f"Closed caption file saved as {file_name}.txt")

# There are several reasons why this script might fail to run or throw an error.
# The API_KEY variable is not set - the script will fail if the API_KEY variable is not set.
# The video ID is not extracted correctly - if the URL is not in the expected format, the code will not be able to extract the video ID.
# The API call fails - if the API call fails due to an incorrect API key or other issue, the script will fail.
# The caption_list variable is empty - if the video does not have any closed captions, the caption_list variable will be empty and the script will fail.
