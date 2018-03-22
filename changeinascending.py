n=int(input('enter'))
a=[]
for i in range(0,n):
  b=int(input('enter the number'))
  a.append(b)
for i in range(n):
  if a[i]>a[i+1]:
    print(a[i-1]+1)
    break
