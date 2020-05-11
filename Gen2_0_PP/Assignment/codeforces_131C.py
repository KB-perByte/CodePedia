def operation(n):
	if n<=1:
		return 1
	p = 1
	for i in range(1,n+1):
		p *= i
	return p

def calc(n,r):
	return operation(n)//operation(r)//operation(n-r)

stdin = input()
n,m,t = stdin.split()
n = int(n)
m = int(m)
t = int(t)

ans = 0

for i in range(4,n+1):
    if(t-i>=1):
        ans += calc(n,i)*calc(m,t-i)

print(ans)