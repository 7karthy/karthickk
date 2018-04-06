a=input("enter")
b=0
for i in a:
  if int(i)%2!=0:
    b=b+int(i)
  else:
    continue
if b%2==0:
  print("E")
elif b==0:
  print('O')
else:
  print('O')
