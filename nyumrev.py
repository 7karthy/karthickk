n=int(input())
re=0
while(n>0):
    dig=n%10
    re=re*10+dig
    n=n//10
print(re)
