class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        firstCity = [a for a, b in costs]
        diff = sorted([b - a for a, b in costs])
        
        return sum(firstCity) + sum(diff[:n])