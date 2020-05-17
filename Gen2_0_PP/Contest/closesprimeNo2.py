
def getPrimes(limit):
    primes = []
    numbers = [True] * limit
    for i in range(2, limit):
        if numbers[i]:
            primes.append(i)
            for n in range(i ** 2, limit, i):
                numbers[n] = False
    return primes


t = int(input())
while(t):
    t-=1
    number = int(input())
    primes = getPrimes(number + 100)
    maxDist = 99999999
    numb = 0
    for p in primes:
        if abs(number - p) < maxDist:
            maxDist = abs(number - p)
            numb = p

    print(numb)
