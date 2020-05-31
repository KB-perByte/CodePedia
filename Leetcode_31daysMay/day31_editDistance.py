from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def func(i, j):
            if i >= m:
                return n - j  # insert the rest of word2[j:]
            elif j >= n:
                return m - i  # delete the rest of word1[i:]
            if word1[i] == word2[j]:
                return func(i + 1, j + 1)
		    # replace, insert, delete, respectively
            return 1 + min(func(i + 1, j + 1), func(i, j + 1), func(i + 1, j))
        
        m, n = map(len, (word1, word2))
        word1, word2 = map(list, (word1, word2))
        return func(0, 0)