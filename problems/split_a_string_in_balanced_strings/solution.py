class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = l = res = 0
        
        for c in s:
            if c == "R": r += 1
            else: l += 1
            
            res += l == r
        
        return res