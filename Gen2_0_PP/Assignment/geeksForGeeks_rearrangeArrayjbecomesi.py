#class sol
def operation(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] < 0:
            continue
        else:
            indx = arr[i]
            val = i
            while(indx != i):
                temp = arr[indx]
                arr[indx] = -1 * (val)
                val = indx
                indx = temp
            arr[indx] = -1 * (val+1)
    return arr

print(operation([1,3,0,2]))
print(operation([2,0,1,4,5,3]))

#mod & div based sol
def operation2(arr):
    n = len(arr)
    for i in range(n): 
        arr[arr[i] % n] += i * n
        
    for i in range(n):
        arr[i] /= n
    return arr

print(operation2([1,3,0,2]))
print(operation2([2,0,1,4,5,3]))

#extra space solution
def operation3(arr):
    n = len(arr)
    temp = [0] * n 
    for i in range(0, n): 
        temp[arr[i]] = i 
    for i in range(0, n): 
        arr[i] = temp[i] 
    return arr

print(operation3([1,3,0,2]))
print(operation3([2,0,1,4,5,3]))