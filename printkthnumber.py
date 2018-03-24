a=int(input('enter range'))
b=[]
for i in range(a):
  c=int(input('enter the number'))
  b.append(c)
k=int(input('enter kth digit'))
print(b[(k-1)])
