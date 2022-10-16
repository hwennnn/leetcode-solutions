class Solution:
    def maxVowels(self, S: str, k: int) -> int:
        d = {"a","e","i","o","u"}
        
        c = res = 0
        
        for i, s in enumerate(S):
            if s in d:
                c += 1
            
            if i >= k and S[i-k] in d:
                c -= 1
            
            res = max(res, c)
        
        return res