a=input('enter')
b=" "
c=" "
index=0
for i in range(len(a)):
  if i%2==0:
    b=b+a[i]
  else:
    c=c+a[i]
print(b,c)
