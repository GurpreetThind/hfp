import time

weekdays = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday' ]
partynight = ['Friday' , 'Saturday']
chillnight = [ 'Sunday' ] 

current_day = time.strftime("%A")


if current_day in weekdays: 
	print("Keep Working")
elif current_day in partynight:
	print("Lite it up")
else:
        print("Chill Night! Before Boring Day Begins")
	
	
