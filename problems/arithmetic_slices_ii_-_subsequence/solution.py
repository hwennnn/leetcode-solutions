class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        res = 0
        dp = [defaultdict(int) for _ in range(n)]
        
        for i in range(1, n):
            for j in range(i):
                dp[i][A[i] - A[j]] += 1
                if A[i] - A[j] in dp[j]:
                    dp[i][A[i] - A[j]] += dp[j][A[i] - A[j]]
                    res += dp[j][A[i] - A[j]]
                    
        return res