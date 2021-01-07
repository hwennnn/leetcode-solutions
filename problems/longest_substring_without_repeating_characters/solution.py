class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = set()
        i = res = 0
        
        for x in s:
            while x in mp:
                mp.remove(s[i])
                i += 1
                
            mp.add(x)
            
            res = max(res, len(mp))
        
        return res