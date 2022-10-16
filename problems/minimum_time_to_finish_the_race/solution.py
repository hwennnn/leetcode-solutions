class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        n = len(tires)
        dp1 = [float('inf')] * 19
        
        for f, r in tires:
            curr = total = f
            dp1[1] = min(dp1[1], total)
            
            for i in range(2, 19):
                curr *= r
                total += curr
                
                if total > 2e5: break
                    
                dp1[i] = min(dp1[i], total)
        
        dp = [float('inf')] * (numLaps + 1)
        
        for i in range(1, numLaps + 1):
            if i < 19:
                dp[i] = dp1[i]
            
            for j in range(1, min(19, i // 2 + 1)):
                dp[i] = min(dp[i], dp[j] + changeTime + dp[i - j])
        
        return dp[numLaps]