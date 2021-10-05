class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [1] + [0] * target
        
        for t in range(target + 1):
            for num in nums:
                if num > t: break
                dp[t] += dp[t - num]
        
        return dp[target]