class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        for i, (d,s) in enumerate(zip(dist, speed)):
            tt = d // s + int(d % s != 0)
            dist[i] = tt
        
        dist.sort()
        res = t = 0

        for tt in dist:
            if tt > t:
                res += 1
            else:
                break
            
            t += 1
        
        return res