class Solution:
    def isPalindrome(self, s: str) -> bool:
        N = len(s)
        i, j = 0, N-1
        while i <= j:
            while not s[i].isalnum() and i < j: i += 1
            while not s[j].isalnum() and i < j: j -= 1
            if s[i] == s[j] or s[i].upper() == s[j].upper():
                i, j = i + 1, j - 1
            else:
                return False
        return True