a=input('enter')
for word in a:
  if a.count(word)>1:
    print(a,'false')
    break
  else:
    print(a,True)
    break
