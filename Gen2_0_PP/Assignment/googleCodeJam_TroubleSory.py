def trouble_sort(arr):
    tArr = [None]*len(arr)
    tArr[::2] = sorted(arr[::2])
    tArr[1::2] = sorted(arr[1::2])
    for i in range(len(tArr)-1):
        if tArr[i] > tArr[i+1]:
            return i
    return 'OK'


if __name__ == '__main__':
    t = int(input())
    for x in range(1, t+1):
        n = int(input())
        arr = list(map(int, input().split()))
        ans = trouble_sort(arr)
        print('Case #{}: {}'.format(x, ans))