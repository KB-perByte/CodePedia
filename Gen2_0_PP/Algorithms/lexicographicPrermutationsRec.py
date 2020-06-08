def genPermutation(num,index):
    if index == len(num)-1:
        print(num)
        return

    for i in range(index, len(num)):
        newList = num[:]
        temp = newList.pop(i)
        newList.insert(index, temp)
        genPermutation(newList, index+1)

genPermutation(['S','a','g','a','r'],0)