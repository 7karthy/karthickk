n=int(input("enter range"))
a=[]
for i in range(0,n):
  c=int(input("enter elements"))
  a.append(c)
a.sort()
b=int(input("enter the kth elements"))
print(a[b-1])
