class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        
        return self.helperR(0, n-1, s, dp)

    def helperR(self, i, j, s, dp):
        if i == j: return 1
        if i > j: return 0
        if dp[i][j]: return dp[i][j]
        
        dp[i][j] = 2 + self.helperR(i+1, j-1, s, dp) if s[i] == s[j] else max(self.helperR(i+1, j, s, dp), self.helperR(i, j-1, s, dp))
        
        return dp[i][j]