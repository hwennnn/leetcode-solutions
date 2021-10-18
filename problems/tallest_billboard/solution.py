class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = collections.defaultdict(int)
        dp[0] = 0
        
        for x in rods:
            nxt = dp.copy()
            for d, y in dp.items():
                nxt[d + x] = max(nxt.get(d + x, 0), y)
                nxt[abs(d - x)] = max(nxt.get(abs(d - x), 0), y + min(d, x))
            
            dp = nxt
        
        return dp[0]