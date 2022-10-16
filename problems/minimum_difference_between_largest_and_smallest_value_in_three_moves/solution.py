class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n <= 4: return 0
        nums = sorted(nums)
        res = float('inf')
        for i in range(4):
            res = min(res, nums[n-1-3+i] - nums[i])
        
        return res