import csv

# Dictionary for storing movie titles, ratings, and times
movies = {}

# Read in CSV
with open('movies.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        movies[row[0]] = {'rating': row[1], 'time': row[2]}

# Initialize customer information
customer_info = {'name': '', 'email': '', 'phone': '', 'card': ''}

# Function to prompt user for information
def prompt_customer_info():
    customer_info['name'] = input('What is your name? ')
    customer_info['email'] = input('What is your email address? ')
    customer_info['phone'] = input('What is your phone number? ')
    customer_info['card'] = input('What is your card number? ')

# Function to prompt user for movie selection
def prompt_movie_selection():
    for movie in movies:
        print(f"{movie}: {movies[movie]['rating']} | {movies[movie]['time']}")
    movie_selection = input('What movie would you like to see? ')
    return movie_selection

# Function to process payment
def process_payment(movie):
    print(f"You have selected {movie}")
    print(f"The cost is ${movies[movie]['rating']}")
    print('Processing payment...')

# Function to print ticket
def print_ticket(movie):
    print('Printing ticket...')
    print(f"{customer_info['name']}")
    print(f"{movie} | {movies[movie]['rating']} | {movies[movie]['time']}")

# Main function
def main():
    prompt_customer_info()
    movie_selection = prompt_movie_selection()
    process_payment(movie_selection)
    print_ticket(movie_selection)

# Call main function
main()

######################################################################

import csv

# Dictionary for storing movie titles, ratings, and times
movies = {}

# Read in CSV
with open('movies.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        movies[row[0]] = {'rating': row[1], 'time': row[2]}

# Initialize customer information
customer_info = {'name': '', 'email': '', 'phone': '', 'card': ''}

# Function to prompt user for information
def get_customer_info():
    customer_info['name'] = input('What is your name? ')
    customer_info['email'] = input('What is your email address? ')
    customer_info['phone'] = input('What is your phone number? ')
    customer_info['card'] = input('What is your card number? ')

# Function to prompt user for movie selection
def get_movie_selection():
    for movie in movies:
        print(f"{movie}: {movies[movie]['rating']} | {movies[movie]['time']}")
    movie_selection = input('What movie would you like to see? ')
    return movie_selection

# Function to process payment
def process_payment(movie):
    print(f"You have selected {movie}")
    print(f"The cost is ${movies[movie]['rating']}")
    print('Processing payment...')

# Function to print ticket
def print_ticket(movie):
    print('Printing ticket...')
    print(f"{customer_info['name']}")
    print(f"{movie} | {movies[movie]['rating']} | {movies[movie]['time']}")

# Main function
def main():
    get_customer_info()
    movie_selection = get_movie_selection()
    process_payment(movie_selection)
    print_ticket(movie_selection)

# Call main function
main()
