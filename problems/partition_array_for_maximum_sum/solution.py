class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        dp = [0] * (N + 1)
        
        for i in range(1, N + 1):
            mmax = 0
            for k in range(1, min(i, K) + 1):
                mmax = max(mmax, A[i - k])
                dp[i] = max(dp[i], dp[i - k] + mmax * k)
        
        return dp[N]