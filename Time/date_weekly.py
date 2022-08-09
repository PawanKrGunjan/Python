import datetime
import calendar
#date = datetime.datetime(2022, 5, 26, 11, 39, 23)
date = datetime.date.today()

for i in range(5):
    date += datetime.timedelta(days=7)
    print(date, calendar.day_name[date.weekday()])
