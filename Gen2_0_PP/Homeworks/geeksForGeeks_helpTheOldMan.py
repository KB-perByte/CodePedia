#code #just a tower of hanoi problem with extra effort

t = int(input())
def towerofhanoi(n, from_disk, to_disk, aux_disk, k, res):
    if n == 1:
        res[0]+=1
        if res[0] == k:
            res.append((from_disk, to_disk))
            return from_disk, to_disk
        return
    
    towerofhanoi(n-1, from_disk, aux_disk, to_disk, k, res)
    res[0]+=1
    if res[0] == k:
            res.append((from_disk, to_disk))
            return from_disk, to_disk
    
    towerofhanoi(n-1, aux_disk, to_disk, from_disk, k, res)

for i in range(t):
    [n, k] = input().split()
    res = [0]
    towerofhanoi(int(n), 1, 3, 2, int(k), res)
    print(res[1][0], res[1][1])
    
    
