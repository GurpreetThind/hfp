from datetime import datetime
import random
import time
odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
for i in range(5):

	right_this_minute = datetime.today().minute
	random_time_for_sleep = random.randint(1,60)
	print(random_time_for_sleep)
	if right_this_minute in odds:
		print("This minute seems little odd")
	else:
		print("Not an odd minute")
	time.sleep(random_time_for_sleep)
