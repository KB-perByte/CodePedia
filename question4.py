
'''
Take a string from user at runtime. Check that using those characters of string is it 
possibletomakeapalindromestring?Ifyesthenprint thepalindromestring.
E.g. abcde O/p: palindrome not possible.
E.g. abcabc O/p: palindrome possible. abccba
'''
NO_OF_CHARS = 256
stir = ''

def isPalindromePossible(st) : 
    count = [0] * (NO_OF_CHARS) 
    for i in range( 0, len(st)) : 
        count[ord(st[i])] = count[ord(st[i])] + 1
    odd = 0
    for i in range(0, NO_OF_CHARS ) : 
        if (count[i] & 1) : 
            odd = odd + 1
        if (odd > 1) : 
            return False
    return True

def isPalindrome(st): 
    if(st == st[:: - 1]):
        return True
    else:
        return False

data = input("Enter a string:")

if(isPalindromePossible(data)):
    print('palindrome possible.')
    if isPalindrome(data):
        print(data)
    else:
        palList = []
        palList = set(data)
        revStr = stir.join(palList)
        freshStr = revStr[::-1] + revStr
        print(freshStr)
else:
    print('palindrome not possible.')
