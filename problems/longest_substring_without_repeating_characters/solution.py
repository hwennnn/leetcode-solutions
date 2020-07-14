class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        d = {}
        
        l = start = 0
        
        for i, char in enumerate(s):
            
            if char in d and start <= d[char]:
                start = d[char] + 1
            
            else:
                l = max(l, i - start + 1)
            
            d[char] = i
        
        return l
            
            
            