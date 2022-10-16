class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res = dp = 0
        prev = -1
        
        for i,x in enumerate(nums):
            if i > 0 and x < left:
                res += dp
            
            if x > right:
                prev = i
                dp = 0
            
            if left <= x <= right:
                dp = i - prev
                res += dp
        
        return res