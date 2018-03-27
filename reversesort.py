n=int(input('enter'))
a=[]
for i in range(n):
  c=int(input('enter the value'))
  a.append(c)
  a.sort(reverse=True)
print(a)
