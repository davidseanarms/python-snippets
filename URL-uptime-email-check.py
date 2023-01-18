#!usr/bin/env python
import requests
import smtplib
import time

url = 'linguahabit.com'
time_interval = 90

email_address = 'me@me.me'

smtp_server = 'smtp.mail.me.com'

smtp_port = 587

smtp_username = 'username'
smtp_password = 'password'

server = smtplib.SMTP(smtp_server, smtp_port)

server.starttls()
server.login(smtp_username, smtp_password)

while True:
    try:
        http_status = requests.get(f'http://{url}')
        http_status.raise_for_status()
    except requests.exceptions.HTTPError as err:
        message = f'HTTP status check failed at {time.asctime()}, HTTP status: {http_status.status_code}'
        server.sendmail(email_address, email_address, message)
    else:
        https_status = requests.get(f'https://{url}')
        https_status.raise_for_status()
    except requests.exceptions.HTTPError as err:
        message = f'HTTPS status check failed at {time.asctime()}, HTTPS status: {https_status.status_code}'
        server.sendmail(email_address, email_address, message)
    time.sleep(time_interval)
server.quit()
