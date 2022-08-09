from datetime import date, timedelta
import calendar
start_date = date.today()
#start_date = date(2014, 12, 25)
for i in range(6):
    days_in_month = calendar.monthrange(start_date.year, start_date.month)[1]
    start_date = start_date + timedelta(days=days_in_month)
    print(start_date, calendar.month_name[start_date.month])
