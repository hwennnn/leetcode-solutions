class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = []
        dry = []
        full = {}
        
        for i, x in enumerate(rains):
            if x == 0:
                dry.append(i)
                res.append(1)
            else:
                if x in full:
                    if not dry: return []
                    
                    index = bisect_right(dry, full[x])
                    if index == len(dry): return []
                    
                    res[dry[index]] = x
                    dry.pop(index)
                    full[x] = i
                    res.append(-1)
                else:
                    full[x] = i
                    res.append(-1)
        
        return res