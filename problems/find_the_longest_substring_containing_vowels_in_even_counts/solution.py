class Solution:
    def findTheLongestSubstring(self, S: str) -> int:
        mp = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        d = {0:-1}
        res = n = 0
        for i, s in enumerate(S):
            if s in mp:
                n ^= mp[s]
            
            if n not in d:
                d[n] = i
            
            else:
                res = max(res, i - d[n])
        
        return res
                