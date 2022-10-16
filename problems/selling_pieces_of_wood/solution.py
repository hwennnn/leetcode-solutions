class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for x, y, price in prices:
            dp[x][y] = price
        
        for w in range(1, m + 1):
            for h in range(1, n + 1):
                for a in range(1, w // 2 + 1):
                    dp[w][h] = max(dp[w][h], dp[w - a][h] + dp[a][h])
                    
                for b in range(1, h // 2 + 1):
                    dp[w][h] = max(dp[w][h], dp[w][h - b] + dp[w][b])
                        
        return dp[m][n]
        
        