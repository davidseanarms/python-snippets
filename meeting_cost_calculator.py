num_attendees = int(input("How many employees will be attending the meeting? "))
avg_salary = float(input("What is the average yearly salary? "))
meeting_hours = int(input("How many hours will the meeting last? "))
cost_per_hour = avg_salary/2080 * num_attendees
print("The cost of a one hour meeting is $%.2f" % cost_per_hour)
cost_per_minute = cost_per_hour/60
print("The cost of the meeting per minute is $%.2f" % cost_per_minute)

#to do: apply Jinja 2 templating for HTML5 output
