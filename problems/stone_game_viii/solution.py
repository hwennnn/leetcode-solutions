class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        
        for i in range(1, n):
            stones[i] += stones[i-1]
            
        dp = stones[-1]
        #since x > 1, the corner is 1, so range(1,)
        for i in range(n - 2, 0, -1):
            dp = max(dp, stones[i] - dp)
            
        return dp