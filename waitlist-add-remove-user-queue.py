# Result:
# John Smith added to wait list.
# Jane Doe added to wait list.
# Current queue length: 2
# Your position in the queue is: 0
# Jane Doe removed from wait list.
# Current queue length: 1
# Notifying John Smith at john@example.com 

# Refactored Code
def add_user(fullname, email):
    user = (fullname, email)
    waitlist.append(user)
    print(f'{fullname} added to wait list.')

def remove_user(fullname):
    for user in waitlist:
        if user[0] == fullname:
            waitlist.remove(user)
            print(f'{fullname} removed from wait list.')
            break

def print_queue_length():
    print(f'Current queue length: {len(waitlist)}')

def print_position(fullname):
    position = 0
    for user in waitlist:
        if user[0] == fullname:
            print(f'Your position in the queue is: {position}')
            break
        position += 1

def notify_top_user():
    if len(waitlist) > 0:
        top_user = waitlist[0]
        print(f'Notifying {top_user[0]} at {top_user[1]}')

waitlist = []

add_user("John Smith", "john@example.com")
add_user("Jane Doe", "jane@example.com")

print_queue_length()

print_position("John Smith")

remove_user("Jane Doe")

print_queue_length()

notify_top_user()
