class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        buckets = [0] * 10001
        
        for x in nums:
            buckets[x] += x
        
        dp = [0] * 10001
        dp[0] = buckets[0]
        dp[1] = buckets[1]
        
        for i in range(2, 10001):
            dp[i] = max(dp[i - 1], dp[i - 2] + buckets[i])

        return dp[-1]