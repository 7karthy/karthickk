a=int(input('enter first num'))
b=int(input('enter second num'))
if a>b:
  if (a-b)%2==0:
    print('yes')
  else:
    print('no')
else:
  if (b-a)%2==0:
    print('yes')
  else:
    print('no')
