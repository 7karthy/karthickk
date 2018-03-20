n=input('enter')
a=""
b=""
for i in range(len(n)):
  c=input('enter the value')
  a=a+c[i]
for i in a:
  count=a.count(i)
  print(count)
  if count>=2:
    b=b+c[i]
  print(b)
if b== " ":
    print('unique')
