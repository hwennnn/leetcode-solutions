class Solution:
    res = float('inf')
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        n = len(toppingCosts)
        
        def helper(current, index):
            
            if abs(target - current) < abs(target - self.res) or (abs(target - current) == abs(target - self.res) and current < self.res):
                self.res = current
            
            if index == n or current > target: return
            
            helper(current, index + 1)
            helper(current + toppingCosts[index], index + 1)
            helper(current + toppingCosts[index] * 2, index + 1)
            
        for base in baseCosts:
            helper(base, 0)
        
        return self.res