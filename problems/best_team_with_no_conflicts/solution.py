class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        players = [[a, s] for a, s in zip(ages, scores)]
        players.sort(reverse = True)
        ans = 0
        dp = [0]*n

        for i in range(n):
            score = players[i][1]
            dp[i] = score
            for j in range(i):
                if players[j][1] >= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + score)
            ans = max(ans, dp[i])
        return ans