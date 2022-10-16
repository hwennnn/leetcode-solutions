class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        res = curr = 0
        
        for a,t in customers:
            curr = max(curr, a) + t
            res += curr - a
        
        return res / n