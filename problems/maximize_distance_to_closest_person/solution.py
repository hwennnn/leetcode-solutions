class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res, last, n = 0, -1, len(seats)
        
        for i,s in enumerate(seats):
            if s:
                res = max(res, i if last == -1 else (i-last) // 2)
                last = i
        
        return max(res, n - last - 1)