class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        m, n = len(queries), len(pattern)
        res = [False] * m
        
        for i, words in enumerate(queries):
            index = 0
            valid = True
            
            for word in words:
                if ord("A") <= ord(word) <= ord("Z") and (index == n or word != pattern[index]):
                    valid = False
                    break
                    
                if index < n and word == pattern[index]:
                    index += 1
            
            res[i] = valid and index == n
        
        return res