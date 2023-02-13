class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        N, M = len(s), len(t)
        j = 0
        leftMost = []

        for i, x in enumerate(s):
            if x == t[j]:
                j += 1
            
            if j == M: return 0

            leftMost.append(j)
        
        res = M
        right = M - 1

        for i in range(N - 1, -1, -1):
            if leftMost[i] <= right:
                res = min(res, right - leftMost[i] + 1)
            
            if s[i] == t[right]:
                right -= 1
            
            res = min(res, right + 1)

        return res
        
