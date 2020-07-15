class Solution:
    def reverseWords(self, s: str) -> str:
        arr = str(s).split()
        return ' '.join(arr[::-1])