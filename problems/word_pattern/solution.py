class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        def hashed(words):
            mp = {}
            res = ""
            
            for index, word in enumerate(words):
                if word not in mp:
                    mp[word] = index
                res += str(mp[word])
            
            return res
        
        return hashed(pattern) == hashed(s.split(' '))
        
        
        
        