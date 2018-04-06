b=int(input('enter'))
a=[]
c=[]
for i in range(b):
  c=int(input("enter num"))
  a.append(c)
for i in range(b):
  if int(i) == a[i]:
    c=str(c)+str(i)
print(sorted(c))
