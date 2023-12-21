import time 
# This is required to include time module.
ticks = time.time()
print ("Number of ticks since 12:00pm, december 16, 2023:", ticks)

print(time.localtime())


localtime = time.localtime(time.time())
print ("Local current time :", localtime)

#getting the formatted time

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

import calendar
cal=calendar.month(2024,3)
print('calender:')
print(cal)


#calendar.calendar(year,w=2,l=1,c=6)

calendar.firstweekday()

calendar.isleap(2013)

calendar.leapdays(2014,2015)




