class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        INF = float('inf')
        
        @cache
        def go(i, prev, k):
            if k > target: return INF
            
            if i == m:
                return 0 if k == target else INF
            
            if houses[i] != 0:
                if houses[i] == prev:
                    return go(i + 1, houses[i], k)
                else:
                    return go(i + 1, houses[i], k + 1)
            
            res = INF
            
            for j, paintCost in enumerate(cost[i]):
                if j + 1 == prev:
                    res = min(res, paintCost + go(i + 1, j + 1, k))
                else:
                    res = min(res, paintCost + go(i + 1, j + 1, k + 1))
            
            return res
        
        ans = go(0, -1, 0)
        return ans if ans != INF else -1