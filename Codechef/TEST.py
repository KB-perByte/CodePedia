m = True
numbLst = []
while m:
    numb = int(input())
    if numb == 42:
        m = False
    else:
        if numb < 100:
            numbLst.append(numb)


for y in numbLst:
    print(y)