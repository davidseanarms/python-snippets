import pymysql

# Establish a connection to the database
mydb = pymysql.connect(
    host="localhost",
    user="username",
    passwd="password",
    database="database_name"
)

# Create a cursor object to execute queries
cursor = mydb.cursor()

# Execute the query to get the user data deletion requests
cursor.execute("SELECT * FROM user_data_deletion_requests")

# Fetch the results
user_data_deletion_requests = cursor.fetchall()

# Close the connection to the database
mydb.close()

# Check if there are any requests made in the last 24 hours
for user_request in user_data_deletion_requests:
    # Get the user request date & time
    user_request_date_time = datetime.datetime.strptime(
        user_request['date_time'], '%Y-%m-%d %H:%M:%S')

    # Calculate the difference between the current date & time and the user request date & time
    time_difference = current_date_time - user_request_date_time
    hours_difference = time_difference.total_seconds() / 3600

    # If the difference is within 24 hours, send out a notification
    if hours_difference <= 24:
        msg = MIMEMultipart()
        msg['From'] = 'sender@gmail.com'
        msg['To'] = 'dataprotectionofficer@company.com'
        msg['Subject'] = 'User Request for Data Deletion'
        body = 'A user with email %s has requested complete account and data deletion.' % user_request['email']
        msg.attach(MIMEText(body, 'plain'))
        smtp_conn.sendmail('sender@gmail.com', 'dataprotectionofficer@company.com', msg.as_string())

# Close the connection to the email
smtp_conn.quit()
