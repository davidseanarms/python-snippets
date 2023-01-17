#!/usr/bin/env python

import datetime

def ask_why(description):
    root_cause = ''
    reason = ''
    for _ in range(5):
        reason = input("Why did it happen? ")
        root_cause = root_cause + ' ' + reason
    description = description + ' The root cause of this issue is: ' + root_cause
    return description

if __name__ == '__main__':
    title, date, start_time, end_time, location, attendees, description = get_inputs()
    description = ask_why(description)
    ical_data = create_ical(title, date, start_time, end_time, location, attendees, description)
    export_ical(ical_data)
    
def get_inputs():
    title = input("Please enter the title of the event: ")
    date = input("Please enter the date of the event (YYYYMMDD): ")
    start_time = input("Please enter the start time of the event (hhmm): ")
    end_time = input("Please enter the end time of the event (hhmm): ")
    location = input("Please enter the location of the event: ")
    attendees = input("Please enter the list of attendees (comma separated email addresses): ")
    description = input("Please enter the description of the event: ")
    return (title, date, start_time, end_time, location, attendees, description)



def create_ical(title, date, start_time, end_time, location, attendees, description):
    ical_data = f"BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//Example Corp.//Calendar Plugin//EN\nBEGIN:VEVENT\nUID:meeting-example-corp-com-{datetime.datetime.now().strftime('%s')}\nSUMMARY:{title}\nDTSTART:{date}T{start_time}\nDTEND:{date}T{end_time}\nLOCATION:{location}\nATTENDEE:{attendees}\nDESCRIPTION:{description}\nEND:VEVENT\nEND:VCALENDAR"
    return ical_data

def export_ical(ical_data):
    f = open("event.ics", "w+")
    f.write(ical_data)
    f.close()
