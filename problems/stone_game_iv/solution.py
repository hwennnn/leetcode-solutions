class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        dp = [False] * (n+1)
        
        for x in range(n+1):
            if not dp[x]:
                y = 1
                while x + y*y <= n:
                    dp[x+y*y] = True
                    y += 1
        
        return dp[n]