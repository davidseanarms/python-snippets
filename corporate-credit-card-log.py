import stripe
import datetime

# Set the Stripe API key
stripe.api_key = 'your_stripe_api_key_here'

# Set up a log file
log_file = 'transaction_log.txt'

# Get the current date and time
now = datetime.datetime.now()

# Get a list of all transactions from the Stripe API
transactions = stripe.Charge.list()

# Loop through each transaction and write the relevant data to the log file
with open(log_file, 'a') as f:
    for transaction in transactions:
        date_time = datetime.datetime.fromtimestamp(transaction.created).strftime('%Y-%m-%d %H:%M:%S')
        amount = transaction.amount / 100
        merchant = transaction.description
        f.write(f'{date_time} ${amount:.2f} {merchant}\n')
```

# This script imports the Stripe library, sets your Stripe API key, and sets up a log file to store the transaction data.
# It then gets the current date and time, gets a list of all transactions from the Stripe API, and loops through each transaction to extract the relevant data.
# Finally, the script appends this data to the log file in the desired format.
# You can run this Python script periodically (e.g. using a cron job) to keep the transaction log up-to-date.
# Please note that this is just an example script and you may need to modify it based on your specific use case and requirements.
