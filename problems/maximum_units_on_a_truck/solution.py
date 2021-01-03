class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : -x[1])
        res = 0
        
        for num,units in boxTypes:
            to_deduct = min(truckSize, num)
            res += units * to_deduct
            truckSize -= to_deduct
        
        return res