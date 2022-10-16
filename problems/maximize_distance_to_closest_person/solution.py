class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        res, last = 0, -1
        
        for i, x in enumerate(seats):
            if x == 1:
                res = max(res, i if last == -1 else (i - last) // 2)
                last = i
        
        res = max(res, n - last - 1)
        
        return res