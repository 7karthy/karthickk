a=int(input("enter a year to find leap year or not"))
if a <1:
    print("invalid")
elif a%4 == 0 :
    print("\nleap year")
else:
    print("\nnot a leap year")
