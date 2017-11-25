# String fromating
from datetime import datetime, date, time, timedelta


template = '{0:.2f} {1:s} is worth US${2:d}'

template.format(2, 'cheese', 12)


dt = datetime(2017, 10, 5, 19, 3, 47)

dt.date()

my_time = dt.time
my_date = dt.date()
print(dt.day)
print(dt.time())

bday = date(1987, 8, 6)
btime = time(7, 35, 13)

# converting datetime object into a String

bday_string = bday.strftime('%d/%m/%Y %H:%S')
print(bday_string)

# there is a difference between small letter and a capital letter
# when foramting datetime, example: %y --> 87, %Y --> 1987

# %H --> hour, %h --> month's first 3 letters

# converting string into datetime object

datetime.strptime('20170806', '%Y%m%d')

# sometimes it will be needed to replace the miuntes and seconds
# with zero. do the following

dt.replace(minute=0, second=0)

difference = timedelta(1, 1, 1, 1, 1, 1, 1)

# Ternary Expressions

# value = true-expr if condition else false-expr

x = 6

sign = 'Posetive' if x > 0 else 'Negative'
print(sign)

# if you want elif statement, need to chain it as follows

sing = "Positive" if x > 0 else 'no sign' if x == 0 else 'Negative'
