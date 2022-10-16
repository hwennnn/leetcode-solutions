class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        nums.sort()
        
        for i, x in enumerate(nums):
            if i > 0 and nums[i] <= nums[i - 1]:
                res += nums[i - 1] - nums[i] + 1
                nums[i] += nums[i - 1] - nums[i] + 1
            
        return res
        