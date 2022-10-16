class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2: return ""
        
        mp = set(list(s))

        for i,c in enumerate(s):
            if c.upper() in mp and c.lower() in mp: continue
            
            first = self.longestNiceSubstring(s[:i])
            second = self.longestNiceSubstring(s[i+1:])
            
            return max(first, second, key = len)
        
        return s