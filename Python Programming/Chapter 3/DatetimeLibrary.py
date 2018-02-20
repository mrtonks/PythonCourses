from datetime import datetime
#You use 'import' to prompt the program to
#retrieve the datetime module

now = datetime.now()
print now

current_year = now.year
current_month = now.month
current_day = now.day

print current_year
print current_month
print current_day

print '%s/%s/%s' %(current_month, current_day, current_year)

print now.hour
print now.minute
print now.second
print '%s:%s:%s' %(now.hour, now.minute, now.second)