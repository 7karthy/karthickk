def reverse(st):
    if len(st) == 0:
        return st
    else:
        return reverse(st[1:]) + st[0]
st=input()
print(reverse(st))
