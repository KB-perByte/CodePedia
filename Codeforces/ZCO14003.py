
def main():
	from sys import stdin, stdout
	rl = stdin.readline

	a = []
	n = int(rl())
	for i in range(n):
		a.append(int(rl()))
	a.sort(reverse=True)
	stdout.write(str(max(x * (i + 1) for i, x in enumerate(a))))

    for i, x in enumerate(a):
        y = max(x*(i+1))

main()    


# noOfInput = long(int(input()))
# customerBudget = []

# for i in range(noOfInput):
#     customerBudget.append(long(input()))

# #for i in sorted(customerBudget):
# customerBudget.sort()
# n = len(customerBudget)//2
# n = n-1 if n%2==0 else n
# lookupArr = customerBudget[n:]
# result = lookupArr[0] * len(lookupArr)
# print(result)

    
