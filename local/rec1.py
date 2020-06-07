def recList(li, i):
    if i < len(li)-1:
        li[i], li[i+1] = li[i+1], li[i]
        recList(li, i+2)
    return li

#print(recList([1,2,3,4,5,6,7],0))

mt2d = [[0,0,1,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,1],
        [0,0,1,0,0,1],
        [0,0,1,0,0,1]]

#TODO
def rec2d(x, i, j):
    
    if x[i][j] == 1 or i == len(mt2d)-1 or j == len(mt2d)-1:
        print('done')
        return
    print(x[i][j], i, j , end = ' -> ')
    rec2d(x, i, j+1)
    rec2d(x, i+1, j)

#rec2d(mt2d, 0, 0)



    

