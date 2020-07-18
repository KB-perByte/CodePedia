'''
x = 29 (00011101) and we want to clear LSB to 3rd bit, total 4 bits
mask -> 1 << 4 -> 16(00010000)
mask -> 16 – 1 -> 15(00001111)
mask -> ~mask -> 11110000
x & mask -> 16 (00010000)
'''

i = 29
mask = ~((1 << i+1 ) - 1)
x &= mask
print(x)

'''
x = 215 (11010111) and we want to clear MSB to 4th bit, total 4 bits
mask -> 1 << 4 -> 16(00010000)
mask -> 16 – 1 -> 15(00001111)
x & mask -> 7(00000111)
'''

mask = (1 << i) - 1
x &= mask
print(x)

'''
x = 18(00010010)
x >> 1 = 9 (00001001)
'''
x >>= 1
print(x)

'''
x = 18(00010010)
x << 1 = 36 (00100100)
'''
x <<= 1

'''
ch = ‘A’ (01000001)
mask = ‘ ‘ (00100000)
ch | mask = ‘a’ (01100001)
'''
ch |= ' '

'''
ch = ‘a’ (01100001)
mask = ‘_ ‘ (11011111)
ch & mask = ‘A’ (01000001)
'''

ch &= '_'


'''
Count set bits in integer
Brian Kernighan’s algorithm.
'''
def countSetBits(x) :
	count = 0
	while (x):
		x &= (x-1) 
		count+=1
	return count


'''
 Find log base 2 of 32 bit integer
'''
def log2(x): 
    res = 0 
    while (x >>= 1):
        res+=1
    return res 

'''
x = 16(000100000)
x – 1 = 15(00001111)
x & (x-1) = 0
so 16 is power of 2
'''
def isPowerof2(x):
	return (x && !(x & x-1))
