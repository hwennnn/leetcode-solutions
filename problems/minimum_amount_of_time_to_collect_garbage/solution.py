class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        lastM = lastP = lastG = -1
        res = 0
        
        for index, gar in enumerate(garbage):
            for gType in gar:
                if gType == "M":
                    lastM = index
                    res += 1
                elif gType == "P":
                    lastP = index
                    res += 1
                else:
                    lastG = index
                    res += 1
        
        for i in range(lastM):
            res += travel[i]
            
        for i in range(lastP):
            res += travel[i]
            
        for i in range(lastG):
            res += travel[i]
            
        return res
        