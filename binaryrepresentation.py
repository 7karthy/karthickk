s=input()
a=len(s)
b=s.count('0')
c=s.count('1')
if (b+c)==a:
  print('yes')
else:
  print('no')
