beginning_value = float(input("What is the beginning value of the investment? "))
ending_value = float(input("What is the ending value of the investment? "))
years = float(input("How many years has the investment been held? "))

# Calculate and print CAGR in percentage
cagr = (ending_value / beginning_value) ** (1 / years) - 1
print(f"The CAGR of the investment is {cagr * 100:.2f} percent.")

# Compound annual growth rate
# Let’s say you invested $1000 in a mutual fund, five years ago. Today, the value of your investment is $1800.
# 1. 1800/1000 = 1.8
# 2. 1.8^1/5 = 1.1474
# 3. 1.1474 - 1 = 0.1474
# 4. 0.1474 * 100 = 14.74%
# The CAGR of your investment is 14.74%.
