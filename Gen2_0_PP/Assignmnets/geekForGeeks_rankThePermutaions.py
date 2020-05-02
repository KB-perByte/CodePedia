'''
crazy way 
'''
import math

def permutation_position_quick(word):
    N = len(word)
    
    first = sorted(word)
    
    chars_before = {
        first[i]: first[:i]
        for i in range(N)
    }
    
    count = 0
    for i in range(N):
        possible_chars = set(chars_before[word[i]])
        possible_chars.difference_update(word[:i])
        n_wildcards = N - (i + 1)
        count += (
          len(possible_chars) * math.factorial(n_wildcards)
        )
    
    return 1 + count

print(permutation_position_quick("ERDOS"))
'''
way 2 
'''

def calRankComp(st, low, high) : 
    countRight = 0
    i = low + 1
    while i <= high : 
        if st[i] < st[low] : 
            countRight = countRight + 1
        i = i + 1
    return countRight 

def randThePermutation(_str): 
    len_str = len(_str) 
    mul = math.factorial(len_str) 
    rank = 1
    i = 0 
    while i < len_str : 
        mul = mul / (len_str - i) 
        countRight = calRankComp(_str, i, len_str-1) 
        rank = rank + countRight * mul 
        i = i + 1
    return rank 

st = input()
print (randThePermutation(st)) 



