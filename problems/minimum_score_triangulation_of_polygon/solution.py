class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        
        @cache
        def go(i, j):
            if j - i + 1 <= 2: return 0
            
            res = float('inf')
            
            for mid in range(i + 1, j):
                res = min(res, values[i] * values[mid] * values[j] + go(i, mid) + go(mid, j))
            
            return res
        
        return go(0, n - 1)