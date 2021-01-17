from datetime import datetime
from datetime import date
from datetime import timedelta

# print today's date and current time
current_date = datetime.now()
print(current_date)

# today's date
today = date.today()
print(today)

# instantiated christmas date
christmas = date(2021, 12, 25)

# number of days before christmas
num_days = christmas - today
print(num_days.days)

# format the time in specific ways
d = datetime(2021, 2, 15, 2, 24)

st1 = d.strftime('%B %d, %Y')
print(st1) #=> January 15, 2021

st2 = d.strftime('%Y/%m/%d')
print(st2) #=> 2021/02/15

st3 = d.strftime('%d %b %y')
print(st3)