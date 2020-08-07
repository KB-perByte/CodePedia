class WordDictionary:

    def __init__(self):
        self.index = {}
        self.words = defaultdict(list)
        
    def compare(self, w1: str, w2: str) -> bool:
        w1 = list(w1)
        w2 = list(w2)
        
        while w1:
            c1 = w1.pop(0)
            c2 = w2.pop(0)
            
            if c1 == '.':
                continue
                
            if c1 != c2:
                return False
            
        
        return True
        
    def addWord(self, word: str) -> None:
        self.index[word] = True
        self.words[len(word)].append(word)
        

    def search(self, word: str) -> bool:
        if word in self.index:
            return True
        
        word_len = len(word)
        
        if word_len not in self.words:
            return False
        
        if word == '.' * word_len:
            return True
        
        words = self.words[word_len]
        for w in words:
            if self.compare(word, w):
                return True
            
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)