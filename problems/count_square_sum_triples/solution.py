class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        mp = collections.defaultdict(int)

        for a in range(1, n + 1):
            for b in range(1, n + 1):
                mp[a * a + b * b] += 1
        
        for c in range(1, n + 1):
            res += mp[c * c]

        
        return res