n=int(input("choose any one:1.+\n2.-\n3.*\n4./\n5.%\n6.square\n7.cube"))
a=float(input("\nenter the first value"))
b=float(input("\nenter the second value\n"))
if  b== 0:
    print("invalid input")
elif n == 1 :
    print(a+b)
elif n == 2 :
    print(a-b)
elif n == 3 :
    print(a*b)
elif n == 4 :
    print(a/b)
elif n == 5 :
    print(a%b)
elif n == 6 :
    print(a**2)
    print(b**2)
elif n == 7 :
    print(a**2)
    print(b**3)
else:
    print("\ninvalid")
