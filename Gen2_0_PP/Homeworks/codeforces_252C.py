n, d = input().split()
n = int(n); d = int(d)
 
a = [int(i) for i in input().split()]
 
def find_index(a, l, val):
	if a[l] - val > d:
		return -1
	r = len(a) - 1
	while l <= r:
		mid = (l+r)//2
		if a[mid] - val > d:
			r = mid-1
		elif a[mid] - val < d:
			l = mid+1
		else:
			return mid
 
	return r
 
i = 0; j = 2
count = 0
while i < n-2:
	pos = find_index(a, j, a[i])
	if pos != -1:
		pos = (pos-i-1) 
	count += (pos*(pos+1))//2
	i += 1; j += 1
 
print(count)