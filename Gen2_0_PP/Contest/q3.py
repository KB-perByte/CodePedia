''' Question 3 - contest 3
Luna took the history of charms class today where she learnt that a spell is proper if the incantation of it spelled in english is a Palindrome.

After the class she visited the restricted section of the library where she found an unusual book on spells. However, the book is very old so some of the letters of the incantations are missing. Help Luna check whether the spell is proper or not.

Input Format

The first line of input contain a single integer T, number of Test Cases.

The first line of each test case contains a single integer n, the length of the string.

The next line of the test case is a string of length n with the missing characters being represented by ?. Rest all characters are lower case english alphabets. Missing character can be replaced by any lower case english alphabet.

Constraints

1 <= T <= 5

1 <= n <= 100

Output Format

Print YES if given string is palindrome else print NO, in the only line of output.

Sample Input 0

2
4
ab?a
5
ab??c
Sample Output 0

YES
NO
'''


def anotherPalindrome1(str1): 
	i = 0
	j = len(str1) - 1
	str1 = list(str1) 
	while (i <= j): 
		if (str1[i] == '?' and str1[j] == '?'): 
			str1[i] = 'a'
			str1[j] = 'a'

		elif (str1[j] == '?'): 
			str1[j] = str1[i] 

		elif (str1[i] == '?'): 
			str1[i] = str1[j] 

		elif (str1[i] != str1[j]): 
			str1 = '' . join(str1) 
			return "NO"

		i += 1
		j -= 1

	str1 = '' . join(str1) 
	return str1 

t = int(input())
while(t):
    t-=1
    n = int(input())
    str1 = str(input())
    x = anotherPalindrome1(str1)
    if x != 'NO':
        print('YES')
    else:
        print('NO')