class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for t in range(1, target + 1):
            for x in nums:
                if x > t: break
                dp[t] += dp[t - x]
        
        return dp[target]