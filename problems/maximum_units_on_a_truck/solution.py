class Solution:
    def maximumUnits(self, A: List[List[int]], truckSize: int) -> int:
        A.sort(key = lambda x : (-x[1], -x[0]))
        res = 0
        
        for k, x in A:
            take = min(k, truckSize)
            truckSize -= take
            res += take * x
        
        return res