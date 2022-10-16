class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        dp = [[n] * n for _ in range(n)]
        
        for x, y in mines:
            dp[x][y] = 0
        
        for i in range(n):
            l = r = u = d = 0
            
            for start, end in zip(range(n), reversed(range(n))):
                l = l + 1 if dp[i][start] != 0 else 0
                dp[i][start] = min(dp[i][start], l)
                
                r = r + 1 if dp[i][end] != 0 else 0
                dp[i][end] = min(dp[i][end], r)
                
                u = u + 1 if dp[start][i] != 0 else 0
                dp[start][i] = min(dp[start][i], u)
                
                d = d + 1 if dp[end][i] != 0 else 0
                dp[end][i] = min(dp[end][i], d)
        
        return max(dp[i][j] for i in range(n) for j in range(n))
        