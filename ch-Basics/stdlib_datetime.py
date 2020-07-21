import datetime

datetime.date.today()

curret_date = datetime.date.today()
print(curret_date)


current_day = datetime.date.today().day
current_month = datetime.date.today().month
current_year = datetime.date.today().year

print(current_day)

print(current_month)

print(current_year)

datetime.date.isoformat(datetime.date.today())



##########Time Module####

import time

current_time = time.strftime("%H:%M")
print(current_time)


current_day_of_week = time.strftime("%A")

is_it_noon = time.strftime("%p") 

print(current_day_of_week , is_it_noon)
