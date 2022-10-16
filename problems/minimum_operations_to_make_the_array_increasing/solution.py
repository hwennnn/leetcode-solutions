class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                d = nums[i - 1] + 1
                res += d - nums[i]
                nums[i] = d
    
        return res