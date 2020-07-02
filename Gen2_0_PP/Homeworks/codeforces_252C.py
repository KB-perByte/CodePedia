N, target = input().split()
N = int(N); target = int(target)
 
a = [int(i) for i in input().split()]
 
def checkIdx(a, l, val):
	if a[l] - val > target:
		return -1
	r = len(a) - 1
	while l <= r:
		mid = (l+r)//2
		if a[mid] - val > target:
			r = mid-1
		elif a[mid] - val < target:
			l = mid+1
		else:
			return mid
 
	return r
 
i = 0; j = 2
count = 0
while i < N-2:
	pos = checkIdx(a, j, a[i])
	if pos != -1:
		pos = (pos-i-1) 
	count += (pos*(pos+1))//2
	i += 1; j += 1
 
print(count)