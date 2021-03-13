class Solution:
    def numFactoredBinaryTrees(self, A: List[int]):
        M = 10 ** 9 + 7
        dp = {}
        
        for a in sorted(A):
            dp[a] = sum(dp[b] * dp.get(a//b, 0) for b in dp if a % b == 0) + 1
        
        return sum(dp.values()) % M