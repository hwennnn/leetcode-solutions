class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        
        n = len(s)
        
        check = [False] * n
        
        for i in range(n):
            for word in words:
                if word == s[i-len(word)+1:i+1] and (check[i-len(word)] or i-len(word) == -1):
                    check[i] = True
        
        return check[-1]