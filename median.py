a=int(input('enter range'))
b=[]
for i in range(a):
  c=input('enter the element')
  b.append(c)
b.sort()
print(b[int(len(b)/2)])
