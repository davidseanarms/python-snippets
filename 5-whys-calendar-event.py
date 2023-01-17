import datetime 

def get_event_info():
    event_title = input("What happened? ")
    # Ask the user why it happened, up to 5 times
    why_happened = ""
    for i in range(1, 6):
        why_happened += input(f"Why {i}? ") 
    # Ask the user for date, start time, length of event, location
    date_str = input("Enter date (dd/mm/yyyy): ")
    start_time_str = input("Enter event start time (24-hour 00:00): ")
    length_str = input("Enter length of event: ")
    location = input("Enter location: ")
    # Convert date, start time, and length to datetime objects
    date_obj = datetime.datetime.strptime(date_str, "%d/%m/%Y")
    start_time_obj = datetime.datetime.strptime(start_time_str, "%H:%M")
    # Create datetime objects for start and end of event
    start_datetime_obj = datetime.datetime.combine(date_obj, start_time_obj.time())
    end_datetime_obj = start_datetime_obj + datetime.timedelta(minutes=int(length_str))
    # Format date and time strings for .ICS file
    start_date_str = start_datetime_obj.strftime("%Y%m%dT%H%M%S")
    end_date_str = end_datetime_obj.strftime("%Y%m%dT%H%M%S")
    # Return event info 
    return event_title, why_happened, start_date_str, end_date_str, location

def create_ics_file(event_title, why_happened, start_date_str, end_date_str, location):
    # Create and open file
    ics_file = open("event.ics", "w")
    # Write file header
    ics_file.write("BEGIN:VCALENDAR\n")
    ics_file.write("VERSION:2.0\n")
    ics_file.write("PRODID:-//Example Corp.//Calendar Plugin//EN\n")
    # Write event info
    ics_file.write("BEGIN:VEVENT\n")
    ics_file.write("UID:meeting-example-corp-com-123456\n")
    ics_file.write(f"SUMMARY:{event_title}\n")
    ics_file.write(f"DTSTART:{start_date_str}\n")
    ics_file.write(f"DTEND:{end_date_str}\n")
    ics_file.write(f"LOCATION:{location}\n")
    ics_file.write(f"DESCRIPTION:{why_happened}\n")
    ics_file.write("END:VEVENT\n")
    ics_file.write("END:VCALENDAR\n")
    # Close file
    ics_file.close()

if __name__ == "__main__":
    event_title, why_happened, start_date_str, end_date_str, location = get_event_info()
    create_ics_file(event_title, why_happened, start_date_str, end_date_str, location)
