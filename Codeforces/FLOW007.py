import  math as m
noOfInput = int(input())
respList = []
def revTheNum(numb):
    revNumb = 0
    while numb:
        revNumb = (revNumb * 10) + (numb % 10)
        numb = numb // 10
    return revNumb

for i in range(noOfInput):
    respList.append(revTheNum(int(input())))

for y in respList:
    print(y)