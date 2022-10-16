class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = 1)
        n = len(cost)
        res = 0
        
        for i in range(n // 3):
            res += cost[i * 3] + cost[i * 3 + 1]
        
        for i in range(n % 3):
            res += cost[-i - 1]
        
        return res