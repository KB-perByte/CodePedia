test_case = int(input())
for test in range(test_case):
    (n, k) = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    ascendingSum1 = 0
    ascendingSum2 = 0
    decendingSum1 = 0
    decendingSum2 = 0
    for i in range(n):
        if i < k:
            ascendingSum1 += arr[i]
        else:
            ascendingSum2 += arr[i]

        if i >= (n - k):
            decendingSum1 += arr[i]
        else:
            decendingSum2 += arr[i]

    diff_asc = abs(ascendingSum1 - ascendingSum2)
    diff_dsc = abs(decendingSum2 - decendingSum1)

    if diff_dsc > diff_asc:
        print(diff_dsc)
    else:
        print(diff_asc)