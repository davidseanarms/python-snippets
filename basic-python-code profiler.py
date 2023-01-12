# This is a basic Python script to ask for a users name and assign them a random number followed by a function to profile the meemory allocated and spent to run the script and output the result.
import random
import time
import sys

def profile_code():
    # Start the timer
    start_time = time.time()
    
    # Ask the user to enter their name 
    name = input("What is your name? ")
    
    # Generate a random number 
    random_number = random.randint(1, 100)
    
    # Print out the result 
    print(f"Hello {name}, your lucky number is {random_number}")
    
    # End the timer
    end_time = time.time()
    
    # Calculate the time spent
    time_spent = end_time - start_time
    
    # Calculate the memory allocated
    memory_allocated = sys.getsizeof(name) + sys.getsizeof(random_number)
    
    # Print the result
    print("Time spent = {:.2f} seconds".format(time_spent))
    print("Memory allocated = {} bytes".format(memory
