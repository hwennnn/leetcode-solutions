class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n & 1: return []
        
        mp = collections.Counter(changed)
        keys = sorted(mp.keys(), reverse = 1)
        res = []
        
        for key in keys:
            if key & 1: continue
            if key == 0 and mp[key] >= 2:
                res += [0] * (mp[key] // 2)
                continue
            
            if key // 2 > 0:
                v = min(mp[key], mp[key // 2])
                mp[key] -= v
                mp[key // 2] -= v

                res += [key // 2] * v

        return res if len(res) == n // 2 else []