t1 = [1,2,-3,4,-5,6,7,-8,-9]
t2 = [1,2,-3,4,-5]
t3 = [-1,-2,-3,-4]
t4 = [1,2,3,4]
t5 = [-1,-2,-3,-4,-5]
t6 = [1,2,3,4,5]
t7 = [1,2,3,-4,-5]
t8 = [-1,-2,3,4]
t9 = [1,2,3,-4,5] #danger zone
t10 = [1,2,3,-4]

def test(num):
    m = []

    for i in range(len(num)-1):
        m.append(num[i]*num[i+1])

    cnt = 0

    for x in m:
        if x > 0:
            cnt+=1

    if cnt == len(num)-1:
        cnt = len(num)//2

    print(cnt)
    return cnt


test(t1)
test(t2)
test(t3)
test(t4)
test(t5)
test(t6)
test(t7)
test(t8)
test(t9)
test(t10)
