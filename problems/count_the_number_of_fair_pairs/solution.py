from sortedcontainers import SortedList

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        res = 0
        sl = SortedList()
        
        for x in nums:
            left = sl.bisect_left(lower - x)
            right = sl.bisect(upper - x)
            res += right - left
            
            sl.add(x)

        return res