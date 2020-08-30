class Solution:
    def checkStraightLine(self, arr: List[List[int]]) -> bool:
        n = len(arr)
        
        x0 = arr[0][0]
        x1 = arr[1][0]
        y0 = arr[0][1]
        y1 = arr[1][1]
        
        for a in arr:
            x, y = a[0], a[1]
            if (x1-x0) * (y-y1) != (y1-y0) * (x-x1):
                return False
        
        return True