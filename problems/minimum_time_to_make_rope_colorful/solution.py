class Solution:
    def minCost(self, S: str, cost: List[int]) -> int:
        
        res = m = s = 0
        
        for i, x in enumerate(S):
            if i > 0 and S[i] != S[i-1]:
                res += s - m
                s = m = 0
            
            s += cost[i]
            m = max(m, cost[i])
        
        res += s - m
        return res
            