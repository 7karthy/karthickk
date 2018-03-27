n=int(input('enter'))
a=[]
b=[]
z=" "
for i in range(n):
  c=input('enter the value')
  a.append(c)
for i in a:
  count=a.count(i)
  #print(count)
  if count>=2:
    b.append(i)
if b==[]:
  print('unique')
else:
  b.sort()
  s=set(b)
  z=' '.join(s)
  print(z)
