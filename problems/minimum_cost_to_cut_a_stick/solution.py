class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + cuts + [n]
        cuts.sort()
        
        @cache
        def go(i, j):
            if j - i <= 1: return 0
            
            res = float('inf')
            
            for k in range(i + 1, j):
                res = min(res, go(i, k) + go(k, j) + cuts[j] - cuts[i])
            
            return res
        
        return go(0, len(cuts) - 1)