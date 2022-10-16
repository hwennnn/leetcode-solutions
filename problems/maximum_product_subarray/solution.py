class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = pos = neg = nums[0]
        
        for x in nums[1:]:
            if x < 0:
                pos, neg = neg, pos
            
            pos = max(x, pos * x)
            neg = min(x, neg * x)
            
            res = max(res, pos)
        
        return res