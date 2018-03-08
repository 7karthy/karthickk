a=int(input('hour1'))
b=int(input('min1'))
c=int(input('hour2'))
d=int(input('min2'))
if a>c:
  a=a-c
  b=b-d
  print(a,b)
else:
  a=c-a
  b=d-b
  print(a,b)
