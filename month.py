import calendar
a=input("enter")
a=a.split("-")
print(a[1])
print(calendar.month_name[int(a[1])])
