class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = curr = nums[0]
        
        for x in nums[1:]:
            curr = max(curr + x, x)
            res = max(res, curr)
        
        return res