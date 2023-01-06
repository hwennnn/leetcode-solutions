class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        N = len(costs)
        costs.sort()
        
        for i, x in enumerate(costs):
            if x > coins: return i

            coins -= x
            
        return N