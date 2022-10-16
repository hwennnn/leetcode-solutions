class WordFilter:

    def __init__(self, words: List[str]):
        self.mp = collections.defaultdict(int)
        self.prefixes = collections.defaultdict(set)
        self.suffixes = collections.defaultdict(set)
        
        for index,word in enumerate(words):
            prefix = ""
            suffix = ""
            
            for char in [""] + list(word):
                prefix += char
                self.prefixes[prefix].add(word)
            
            for char in [""] + list(word[::-1]):
                suffix += char
                self.suffixes[suffix[::-1]].add(word)
            
            self.mp[word] = index

    def f(self, prefix: str, suffix: str) -> int:
        res = -1
        
        for word in self.prefixes[prefix] & self.suffixes[suffix]:
            res = max(res, self.mp[word])
        
        return res


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)