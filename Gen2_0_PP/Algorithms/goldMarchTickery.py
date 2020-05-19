print('To find sum of all the elements in a given range')
maxNum = float('-inf')
maxVal = 10**6

arr = [0] * maxVal
queries = int(input('No. of test cases:'))

while(queries):
    queries-=1
    print('value of L and R till which each element will be incremeted by 1:')
    inp = list(map(int, input().split()))
    arr[inp[0]]+=1
    arr[inp[1]+1]-=1

print('Get i.th value:')
sum = 0
for x in range(int(input())):
    sum += arr[x]

print('i.th value:', sum)



    



