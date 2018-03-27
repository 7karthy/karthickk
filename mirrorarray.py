n=int(input('enter FIRST'))
a=[]
for i in range(n):
  c=int(input('enter the value'))
  a.append(c)
  a.sort(reverse=True)
m=int(input('enter second'))
b=[]
for i in range(n):
  d=int(input('enter the value'))
  b.append(d)
if a==b:
  print("yes")
else:
  print("no")
