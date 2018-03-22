a=input("enter value")
b=0
for i in range(len(a)):
  b+=int(a[i])**(len(a))
if a==str(b):
  print("yes")
else:print("no")
