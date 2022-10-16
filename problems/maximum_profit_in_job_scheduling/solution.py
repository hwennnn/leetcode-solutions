class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profits: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profits), key = lambda x : x[1])
        dp = [[0, 0]]
        
        for start, end, profit in jobs:
            i = bisect.bisect(dp, [start + 1]) - 1
            
            if dp[i][1] + profit > dp[-1][1]:
                dp.append([end, dp[i][1] + profit])
        
        return dp[-1][1]