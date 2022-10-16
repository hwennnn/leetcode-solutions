from sortedcontainers import SortedList

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        largest = SortedList()
        res = i = costs = 0
        
        for j in range(n):
            largest.add(chargeTimes[j])
            costs += runningCosts[j]
            
            total = largest[-1] + (j - i + 1) * costs
            
            while total > budget:
                largest.remove(chargeTimes[i])
                costs -= runningCosts[i]
                i += 1
                total = largest[-1] if largest else 0 + (j - i + 1) * costs
                
            res = max(res, j - i + 1)
        
        return res