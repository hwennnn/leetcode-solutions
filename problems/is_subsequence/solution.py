class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        i = 0
        
        for x in t:
            if i < n and x == s[i]:
                i += 1
            
            if i == n:
                break
        
        return i == n