nu = int(input("Enter a number: "))
if nu > 1:
   for i in range(2,nu):
       if (nu % i) == 0:
           print("yes")
           break
   else:
       print("no")
else:
   print("yes")
