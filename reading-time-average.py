def calculate_reading_time(words):
    # Calculate the time to read a text in minutes
    reading_speed = 250  # Average adult reading speed (words per minute)
    reading_time = words / reading_speed  # Reading time in minutes
    return reading_time

# Main program
words = int(input("Enter the number of words: "))
print("Reading time: {:.2f} minutes".format(calculate_reading_time(words)))
