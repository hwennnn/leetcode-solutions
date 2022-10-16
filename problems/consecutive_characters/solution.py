class Solution:
    def maxPower(self, s: str) -> int:
        n = len(s)
        curr = s[0]
        count = res = 1
        
        for i in range(1, n):
            if s[i] == curr:
                count += 1
            else:
                count = 1
                curr = s[i]
            
            res = max(res, count)
        
        return res