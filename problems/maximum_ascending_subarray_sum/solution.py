class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = total = nums[0]
        n = len(nums)
        
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                total += nums[i]
            else:
                total = nums[i]
            
            res = max(res, total)

        return res