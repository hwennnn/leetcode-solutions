class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats = corridor.count("S")
        M = 10 ** 9 + 7
        
        if seats & 1 or seats < 2: return 0
        
        s = [i for i, x in enumerate(corridor) if x == "S"]
        
        res = 1
        for i in range(1, len(s) - 1, 2):
            res *= (s[i + 1] - s[i])
            
        return res % M
            