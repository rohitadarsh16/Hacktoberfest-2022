import calendar
year = int(input())
month = int(input())
s = calendar.TextCalendar(calendar.SUNDAY)
print(s.formatmonth(year,month))
