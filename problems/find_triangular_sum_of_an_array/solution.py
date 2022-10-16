class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        for _ in range(n - 1):
            curr = []
            
            for i in range(1, len(nums)):
                curr.append((nums[i - 1] + nums[i]) % 10)
            
            nums = curr
        
        return nums[0]