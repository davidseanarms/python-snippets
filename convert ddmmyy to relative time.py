# Refactored 09/12/22
import datetime

def convert_date(date):
    date_obj = datetime.datetime.strptime(date, '%d/%m/%Y')
    diff = datetime.datetime.today() - date_obj
    years = diff.days // 365
    months = (diff.days % 365) // 30
    days = diff.days % 30
    if years > 0:
        return f"{years} year(s), {months} month(s) and {days} day(s) ago"
    elif months > 0:
        return f"{months} month(s) and {days} day(s) ago"
    else:
        return f"{days} day(s) ago"

date_str = "16/05/1988"
print(convert_date(date_str))
