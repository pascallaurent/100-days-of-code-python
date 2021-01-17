from datetime import datetime
from datetime import timedelta
from datetime import date

birthday = date(2021, 10, 18)
today = date.today()
number_of_days = (birthday - today).days

date_time = datetime.now() + timedelta(days=number_of_days)


print(f'In {number_of_days} I am celebrating my  birthday at : \
  {date_time.strftime("%H:%M:%S")}' )