# Refactored Code
# set max occupancy
MAX_OCCUPANCY = 150

# set current occupancy
current_occupancy = 135

# define sensor logic
def sensor_logic(current_occupancy):
    if current_occupancy == MAX_OCCUPANCY:
        print("Max occupancy of 150 people reached")
    elif current_occupancy < MAX_OCCUPANCY:
        print(f"One shopper has entered, occupancy is now: {current_occupancy + 1}")
    elif current_occupancy > 0:
        print(f"One shopper has left, occupancy is now: {current_occupancy - 1}")
    else:
        print("No shoppers in the supermarket")

# set sensor logic
sensor_logic(current_occupancy)
