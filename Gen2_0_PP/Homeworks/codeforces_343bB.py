s = input().strip()
a = ['K']
for i in s:
    if a[-1]==i:
        a.pop()
    else:
        a.append(i)
if len(a)==1:
    print("Yes")
else:
    print("No")


#try 2

s=[]
for i in input():
    if s and s[-1]==i:s.pop()
    else:s.append(i)
print('Yneos'[bool(s)::2])