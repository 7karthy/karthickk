n= int(input("Please Enter any Number: "))
s= 0
while(n> 0):
  r= n% 10
  s= s+r
  n= n//10
print(s)
