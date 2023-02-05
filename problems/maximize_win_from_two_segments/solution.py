class Solution:
    def maximizeWin(self, nums: List[int], k: int) -> int:
        N = len(nums)
        dp = [0] * (N + 1)
        i = 0
        res = 0
        
        for j, x in enumerate(nums):
            while nums[i] < nums[j] - k:
                i += 1
            
            dp[j + 1] = max(dp[j], j - i + 1)
            res = max(res, j - i + 1 + dp[i])
        
        return res