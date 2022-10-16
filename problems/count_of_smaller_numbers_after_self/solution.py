from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        sl = SortedList([nums[-1]])
        
        for i in range(n - 2, -1, -1):
            index = sl.bisect(nums[i] - 1)
            
            res[i] = index
            
            sl.add(nums[i])
        
        return res