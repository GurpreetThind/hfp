#Creating a date time object and extract the minute attribute before assigning it to the variable 
from datetime import datetime

time_now = datetime.today()
print(time_now)

right_this_minute = time_now.minute

print(right_this_minute)
