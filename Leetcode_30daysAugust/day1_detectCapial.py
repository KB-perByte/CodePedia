class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        def is_capital(character):
            return ord('A') <= ord(character) <= ord('Z')
        
        all_capital = all([is_capital(char) for char in word])
        all_non_capital = all([not is_capital(char) for char in word[1:]])
        
        return all_capital or all_non_capital