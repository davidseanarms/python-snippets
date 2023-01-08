initial_issue = input('What is the initial issue? ')
counter = 1
while counter <= 5:
    why_question = input('Why did this happen? ')
    counter += 1
print(f'The root cause of the {initial_issue} is {why_question}')
print(f'Summary: The initial problem was {initial_issue} and the root cause was {why_question}')
date_input = input("Please enter date in dd/mm/yyyy format: ")
time_input = input("Please enter time in 24-hour (military) time format: ")
calendar_event = why_question
with open('calendar_event.ico', 'w') as f:
    f.write(f'{calendar_event},{date_input},{time_input}')
print('Exported .ico file successfully!')
