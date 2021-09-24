class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = pos = neg = nums[0]
        
        for i in range(1, len(nums)):
            
            if nums[i] < 0:
                pos, neg = neg, pos
            
            pos = max(nums[i], pos * nums[i])
            neg = min(nums[i], neg * nums[i])
            
            res = max(res, pos)
        return res