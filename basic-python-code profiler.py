# This is a basic Python script to ask for a users name and assign them a random number
# followed by a function to profile the meemory allocated and spent to run the script and output the result.

import random
import time
import sys

def profile_code():

    start_time = time.time()
    
    name = input("What is your name? ")
    random_number = random.randint(1, 100)
    print(f"Hello {name}, your lucky number is {random_number}")

    end_time = time.time()
    
    time_spent = end_time - start_time
    
    memory_allocated = sys.getsizeof(name) + sys.getsizeof(random_number)
    
    print("Time spent = {:.2f} seconds".format(time_spent))
    print("Memory allocated = {} bytes".format(memory
