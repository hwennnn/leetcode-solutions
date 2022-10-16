class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        dp = [0] * n
        
        for i in range(1, n):
            dp[i] = (2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2) % (10 ** 9 + 7)
        
        return dp[-1]