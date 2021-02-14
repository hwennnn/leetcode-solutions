class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        
        res = []
        prefix = [0] + list(accumulate(candiesCount))
            
        for favType, day, cap in queries:
            if (day+1) * cap > prefix[favType] and prefix[favType+1] >= (day+1) * 1:
                res.append(True)
            else:
                res.append(False)
            
        return res