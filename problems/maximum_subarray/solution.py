class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, curr = float('-inf'), 0
        
        for x in nums:
            curr = max(curr + x, x)
            res = max(res, curr)
        
        return res