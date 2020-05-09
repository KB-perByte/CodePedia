#a = 3985
a = 1305060
arr = []
cnt = 0
while(a):
    cnt += 1
    if a%10 != 0:
        arr.append((a%10))
        print((a%10)*(10**cnt))
        a//=10
        #print(a)
    a//=10
print(arr)