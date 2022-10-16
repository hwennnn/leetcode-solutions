class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        prefix = [0] + list(accumulate(stones))
        
        def dfs(i, j):
            if i == j: return 0
            if dp[i][j]: return dp[i][j]
            
            ssum = prefix[j + 1] - prefix[i]
            dp[i][j] = max(ssum - stones[i] - dfs(i + 1, j), ssum - stones[j] - dfs(i, j - 1))
            
            return dp[i][j]
        
        return dfs(0, n - 1)