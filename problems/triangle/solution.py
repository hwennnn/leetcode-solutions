class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        n = len(t)
        
        for i in reversed(range(n-1)):
            for j in range(len(t[i])):
                left, right = t[i + 1][j], t[i + 1][j + 1]
                t[i][j] += min(left, right)
        
        return t[0][0]