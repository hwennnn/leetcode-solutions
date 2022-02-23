class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = dict()
        dp[0] = 0
        
        for x in rods:
            curr = defaultdict(int)
            
            for s in dp:
                curr[s + x] = max(curr[s + x], dp[s] + x)
                curr[s] = max(curr[s], dp[s])
                curr[s - x] = max(curr[s - x], dp[s])
                
            dp = curr
        
        return dp[0]