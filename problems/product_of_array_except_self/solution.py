class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]
        for x in nums:
            left.append(left[-1] * x)
        
        res = [0] * n
        right = 1
        
        for i in range(n - 1, -1, -1):
            res[i] = right * left[i]
            right *= nums[i]
        
        return res