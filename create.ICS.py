import datetime

# User input
title = input('Meeting title: ')
date_input = input('Date (dd/mm/yyyy): ')
start_time = input('Meeting start time (hh:mm): ')
length_minutes = int(input('Meeting Length (minutes): '))
location = input('Meeting location: ')
email = input('Invitee email: ')

# Calculate meeting end time
start_time_dt = datetime.datetime.strptime(start_time, '%H:%M')
end_time_dt = start_time_dt + datetime.timedelta(minutes=length_minutes)
end_time = end_time_dt.strftime('%H:%M')

# Generate ICS file
ics_file = f'''BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//hacksw/handcal//NONSGML v1.0//EN
BEGIN:VEVENT
UID:meeting_{title}
DTSTAMP:{date_input}T{start_time}
ORGANIZER;CN=Me:MAILTO::{email}
DTSTART:{date_input}T{start_time}
DTEND:{date_input}T{end_time}
SUMMARY:{title}
LOCATION:{location}
END:VEVENT
END:VCALENDAR'''

# Export ICS file
with open(f'{title}.ics', 'w') as f:
    f.write(ics_file)
    print(f'{title}.ics created.')
