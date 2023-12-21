
from datetime import date


# Getting min date
mindate = date.min
print("Minimum Date:", mindate)


# Getting max date
maxdate = date.max
print("Maximum Date:", maxdate)


Date1 = date(2023, 4, 20)
print("Year:", Date1.year)
print("Month:", Date1.month)
print("Day:", Date1.day)

print (date.today())
d1=date.fromisoformat('2023-04-20')
print (d1)
d2=date.fromisoformat('20230420')
print (d2)
d3=date.fromisoformat('2023-W16-4')
print (d3)


d = date.fromordinal(738630) # 738630th day after 1. 1. 0001
print (d)
print (d.timetuple())
# Methods related to formatting string output
print (d.isoformat())
print (d.strftime("%d/%m/%y"))
print (d.strftime("%A %d. %B %Y"))
print (d.ctime())


print ('The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month"))


# Methods for to extracting 'components' under different calendars
t = d.timetuple()
for i in t:
   print(i)
   
ic = d.isocalendar()
for i in ic:
   print(i)
   
# A date object is immutable; all operations produce a new object
print (d.replace(month=5))


from datetime import datetime
dt = datetime.now()


print("Day: ", dt.day)
print("Month: ", dt.month)
print("Year: ", dt.year)
print("Hour: ", dt.hour)
print("Minute: ", dt.minute)
print("Second: ", dt.second)


from datetime import timedelta
delta = timedelta(
   days=100,
   seconds=27,
   microseconds=10,
   milliseconds=29000,
   minutes=5,
   hours=12,
   weeks=2
)
# Only days, seconds, and microseconds remain
print (delta)