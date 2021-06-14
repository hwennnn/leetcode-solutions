class Solution:
    def maximumUnits(self, boxes: List[List[int]], truckSize: int) -> int:
        boxes.sort(key = lambda x: (-x[1]))
        res = 0
        
        for box, unit in boxes:
            m = min(box, truckSize)
            res += m * unit
            truckSize -= m
            
            if truckSize == 0: break
        
        return res