class Solution:
    def countPairs(self, A: List[int]) -> int:
        M = 10 ** 9 + 7
        res = 0
        mp = Counter(A)
        
        for i in range(22):
            p = 1 << i
            for v in mp:
                target = p - v
                if v == target:
                    res += mp[v] * (mp[v]-1)
                else:
                    res += mp[v] * mp[target]
        
        res //= 2
        
        return res % M