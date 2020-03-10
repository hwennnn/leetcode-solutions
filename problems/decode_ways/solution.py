class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0
        len_s = len(s)
        dp = [1] + [0] * len_s
        for i in range(1, len_s + 1):
            if s[i - 1] != '0': 
                dp[i] += dp[i - 1]
            if i >= 2 and 10 <= int(s[i - 2: i]) <= 26: 
                dp[i] += dp[i - 2]
        return dp[len_s]