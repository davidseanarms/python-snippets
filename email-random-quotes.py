#!/usr/bin/env python

import random
import smtplib

email = raw_input("Enter your email address: ")

quotes = [
    "Life is 10% what happens to you and 90% how you react to it. - Charles R. Swindoll",
    "Success is not final; failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "If you want to lift yourself up, lift up someone else. - Booker T. Washington",
    "You can never cross the ocean until you have the courage to lose sight of the shore. - Christopher Columbus"
]

for i in range(5):
    quote = random.choice(quotes)

    # Create an SMTP object
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to the email server
    server.login("your_email_address", "your_password")

    # Send the email
    server.sendmail("your_email_address", email, quote)

    # Close the connection
    server.quit()
