class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        desired = n // 4
        c = Counter(s)
        
        for key in c:
            if c[key] > 0:
                c[key] = max(0, c[key] - desired)
        
        res = n
        i = 0
        
        for j,x in enumerate(s):
            c[x] -= 1
            
            while i < n and all(val <= 0 for val in c.values()):
                res = min(res, j - i + 1)
                c[s[i]] += 1
                i += 1
        
        return res