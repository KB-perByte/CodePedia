
def allPrimes(n):
    if n <= 2:
        return 0
    else:
        upperlimit = int(n ** 0.5)
        candidates = [True] * n
        candidates[0] = False
        candidates[1] = False
        for i in range(2, min(upperlimit + 1, n)):
            if candidates[i]:  # that means i is prime
                cleanLoc = 2 * i
                while cleanLoc < n:
                    candidates[cleanLoc] = False
                    cleanLoc += i
        return candidates

isPrime = allPrimes(1000011)
testCases = int(input())
while testCases > 0:
    testCases -= 1
    n = int(input())
    lookLeft = n
    while lookLeft >= 0 and not isPrime[lookLeft]:
        lookLeft -= 1
    smallerPrime = lookLeft # either -1 or the actual prime
    lookRight = n + 1
    while lookRight < 1000011 and not isPrime[lookRight]:
        lookRight += 1
    biggerPrime = lookRight
    myPrime = biggerPrime
    if smallerPrime > 0 and smallerPrime + biggerPrime >= 2 * n:
        myPrime += smallerPrime - biggerPrime
    print(myPrime)