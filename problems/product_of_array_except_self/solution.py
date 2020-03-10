class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        left = [None] * n
        left[0] = 1
        output = [None] * n
        
        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]
            
        R = 1
            
        for i in range(n-1,-1,-1):
            output[i] = left[i] * R
            R = nums[i] * R
            
        return output