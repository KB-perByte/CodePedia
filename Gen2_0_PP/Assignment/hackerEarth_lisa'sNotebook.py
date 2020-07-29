'''
countr = 0
indx = 1
def bookCrawl(_chp , chp, k, rangeL, rangeR):
    global countr
    global indx
    
    if rangeR >= _chp:
        indx += 1
        if rangeR == _chp:
            countr += 1
        return countr
    if rangeL<=indx and indx <= rangeR:
        countr += 1
    indx += 1
    bookCrawl(_chp, chp-k, k, rangeL+k, rangeR+chp) 

if __name__ == '__main__':
    t = int(input())
    for x in range(1, t+1):
        ans = 0
        _n = list(map(int, input().split()))
        n ,k = _n[0], _n[1] 
        arr = list(map(int, input().split()))
        for i, c in enumerate(arr):
            a = bookCrawl(c, c, k, 1, k)
            if a:
                ans+=a
        print(ans)
'''

#try 2
'''
count = 0
page = 1
if __name__ == '__main__':
    t = int(input())
    for x in range(1, t+1):
        ans = 0
        _n = list(map(int, input().split()))
        n ,k = _n[0], _n[1] 
        arr = list(map(int, input().split()))
        for ch in arr:
            for ch in range(1,ch + 1):
                if(page == ch):
                    count = count + 1
                if ((ch % k == 0 )or ch == ch):
                    page = page + 1         
        print(count)
'''

_n = list(map(int, input().split()))
n ,k = _n[0], _n[1] 
arr = list(map(int, input().split()))

cnt = 0
chapter = 0
page = 1
prob = 1
if __name__ == '__main__':
    while chapter < n:
        if prob <= page and page <= min(prob + k - 1, arr[chapter]):
            cnt += 1
        page += 1
        prob += k
        if prob > arr[chapter]: 
            chapter += 1
            prob = 1
    print(cnt) 