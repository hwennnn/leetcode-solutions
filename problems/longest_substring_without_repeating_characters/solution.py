class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i = 0
        res = 0
        
        for j, x in enumerate(s):
            while x in seen:
                seen.remove(s[i])
                i += 1
            
            seen.add(x)
            
            res = max(res, j - i + 1)
            
        return res
            