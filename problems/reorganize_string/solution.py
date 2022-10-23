class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        pq = []
        res = []
        
        for k, v in counter.items():
            heappush(pq, (-v, k))
        
        while pq:
            v, k = heappop(pq)
            v = -v
            
            if len(res) == 0 or res[-1] != k:
                res.append(k)
                if v - 1 > 0:
                    heappush(pq, (-(v - 1), k))
            else:
                if not pq: return ""
                v2, k2 = heappop(pq)
                v2 = -v2
                
                res.append(k2)
                if v2 - 1 > 0:
                    heappush(pq, (-(v2 - 1), k2))
                
                heappush(pq, (-v, k))
        
        return "".join(res)