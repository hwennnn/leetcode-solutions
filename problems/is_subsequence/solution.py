class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        loop = iter(t)
        
        return all(w in loop for w in s)