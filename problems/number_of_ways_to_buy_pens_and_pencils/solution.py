class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        
        
        if cost2 > cost1:
            cost1, cost2 = cost2, cost1
        
        res = 0
        
        for buy in range(total // cost1 + 1):
            curr = total - (buy * cost1)
            res += (curr // cost2) + 1
        
        return res