class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        
        for c in s+t:
            res ^= ord(c)
            
        return chr(res)