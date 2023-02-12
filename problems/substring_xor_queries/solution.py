class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        N = len(s)
        lookup = {}
        
        for k in range(1, 33):
            mask = (1 << k) - 1
            curr = 0
            
            for i, x in enumerate(s):
                curr <<= 1
                curr += int(x)
                curr &= mask
            
                if curr not in lookup:
                    lookup[curr] = [i - k + 1, i]
        
        res = []
        for a, b in queries:
            t = a ^ b
            
            if t not in lookup:
                res.append([-1, -1])
            else:
                res.append(lookup[t])
        
        return res