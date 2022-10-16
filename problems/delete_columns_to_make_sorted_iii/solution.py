class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        n = len(A[0])
        dp = [1] * n
        
        for j in range(1, n):
            for i in range(j):
                if all(a[j] >= a[i] for a in A):
                    dp[j] = max(dp[j], dp[i] + 1)
            
        return n - max(dp)