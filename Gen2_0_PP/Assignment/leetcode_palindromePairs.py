class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def prefixes(word):
            for i in range(len(word) + 1):  
                string, prefix = word[:i], word[i:]
                if string == string[::-1]:
                    yield prefix

        def suffixes(word):
            for i in range(len(word)): 
                suffix, string = word[:i], word[i:]
                if string == string[::-1]:
                    yield suffix

        cache = {string[::-1]: idx for idx, string in enumerate(words)}

        for idx, string in enumerate(words):
            for prefix in prefixes(string):
                if prefix in cache and idx != cache[prefix]:
                    yield [cache[prefix], idx]

            for suffix in suffixes(string):
                if suffix in cache and idx != cache[suffix]:
                    yield [idx, cache[suffix]]