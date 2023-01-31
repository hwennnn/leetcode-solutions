class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        N = len(scores)
        A = [(a, s) for s, a in zip(scores, ages)]
        A.sort()
        res = 0
        dp = [0] * (N + 1)

        for i in range(N):
            dp[i] = A[i][1]

            for j in range(i):
                if A[j][1] <= A[i][1]:
                    dp[i] = max(dp[i], dp[j] + A[i][1])
            
            res = max(res, dp[i])
        
        return res