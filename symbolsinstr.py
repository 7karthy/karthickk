s="~`!@#$%^&*()_-+={}[]:>;',</?*.-+"
a=input('enter a string')
count=0
for i in a:
  if(i in s):
    count=count+1
print(count)
