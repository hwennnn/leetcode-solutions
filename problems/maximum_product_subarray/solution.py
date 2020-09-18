class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        pos = neg = res = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > 0:
                pos = max(pos*nums[i], nums[i])
                neg = min(neg*nums[i], nums[i])
            
            else:
                temp = pos
                pos = max(neg*nums[i], nums[i])
                neg = min(temp*nums[i], nums[i])
        
            res = max(res, pos)
        
        return res