def mergeInter(arr1, arr2):
    arrX= []
    a,b = len(arr1), len(arr2)
    max_l = b if b>=a else a

    for i in range(max_l):
        if i <= a-1:
            arrX.append(arr1[i])
        if i <= b-1:
            arrX.append(arr2[i])

    return arrX

a1 = [1,3, 5, 7, 9]
a2 = [2, ]
print(mergeInter(a1, a2))
