class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        res = 0
        n = len(colors)
        
        for i in range(n):
            for j in range(i + 1, n):
                if colors[i] != colors[j]:
                    res = max(res, j - i)
        
        return res
            