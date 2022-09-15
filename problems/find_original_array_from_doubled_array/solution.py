class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        N = len(changed)
        if N & 1: return []
        
        res = []
        counter = Counter(changed)
        
        for k in sorted(counter.keys(), reverse = 1):
            if k & 1: continue
                
            if k == 0 and counter[k] >= 2:
                res += [k] * (counter[k] // 2)
                continue
                
            half = k // 2
            if half > 0:
                v = min(counter[k], counter[half])
                counter[half] -= v
                
                res += [half] * v

        if len(res) != N // 2:
            return []
        
        return res