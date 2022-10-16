class Solution:
    def countPoints(self, rings: str) -> int:
        mp = collections.defaultdict(set)
        n = len(rings)
        
        for i in range(0, n, 2):
            mp[rings[i + 1]].add(rings[i])
        
        res = 0
        
        for k, v in mp.items():
            if len(v) == 3:
                res += 1

        return res
        