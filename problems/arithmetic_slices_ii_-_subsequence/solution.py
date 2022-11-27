class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [defaultdict(int) for _ in range(N)]
        res = 0

        for i in range(1, N):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1

                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    res += dp[j][diff]
        
        return res