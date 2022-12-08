# Asks for monthly income.
# Asks for monthly rent and electricity expenses.
# Outputs $ and % available to invest if investing 25% of remaining income.
# Calculates 12-month return if investing at 6.5% returns.

# ask for monthly income
income = float(input("What is your monthly income? "))

# ask for rent and electricity bill
rent = float(input("What is your monthly rent? "))
electricity = float(input("What is your monthly electricity bill? "))

# calculate remaining amount to invest
remaining = income - (rent + electricity)
investment = remaining * 0.25

# output remaining amount to invest
print("You have ${0:.2f} to invest".format(investment))

# calculate 12-month return on investment
monthly_returns = investment * 0.065
total_returns = monthly_returns * 12

# output 12-month returns on investment
print("Your 12-month returns would be ${0:.2f}".format(total_returns))
