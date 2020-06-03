'''2  162
                                2
                            8       21 
                        16     81 
                    32      161   
                64      xx       xx
            128     xx
        xx      xx
'''


ans = []
flag = 1

def helper(i):
    global flag, m, n, ans 
    
    if flag == 0:
        return

    if i == m:
        flag = 0
        print("YES")
        print(len(ans) + 1)
        print(n , end = ' ')
        for j in range(len(ans)):
            print(ans[j], end = ' ')
        return

    if i > m:
        return

    print(ans)
    ans.append(i * 2)
    helper(i * 2)
    ans.pop()
    print(ans)
    ans.append(i * 10 + 1)
    helper(i * 10 + 1)
    ans.pop()

n, m = map(int, input().split())
helper(n)
if flag == 1:
    print('NO')