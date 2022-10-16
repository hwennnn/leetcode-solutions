class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        seen = {}
        res = v = 0
        
        for i, h in enumerate(hours):
            v = v + 1 if h > 8 else v - 1
                        
            if v > 0:
                res = i + 1
                
            seen.setdefault(v, i)

            if v - 1 in seen:
                res = max(res, i - seen[v - 1])
        
        return res