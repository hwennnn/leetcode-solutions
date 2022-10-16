class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        if not nums: return 0
        
        n = len(nums)
        
        dp = [1] * n
        
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
                
        return max(dp)
        