class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def h(word):
            s = {}
            res = []
            
            for x in word:
                if x not in s:
                    s[x] = len(s)
                    
                res.append(s[x])
            
            return "".join(map(str, res))
        
        target = h(pattern)
        res = []
        
        for word in words:
            if h(word) == target:
                res.append(word)
        
        return res