class Solution(object):
    def findPoisonedDuration(self, ts, d):
        n = len(ts)
        if n == 0: return 0
        
        res = d
        
        for i in range(1, n):
            if ts[i] - ts[i-1] > d:
                res += d
            else:
                res += ts[i] - ts[i-1]
        
        return res
        