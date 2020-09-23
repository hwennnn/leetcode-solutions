class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = totalCost = res = cur = 0
        
        for i, (g,c) in enumerate(zip(gas,cost)):
            totalGas += g
            totalCost += c
            cur += (g-c)
            if cur < 0:
                cur = 0
                res = i+1
        
        return -1 if totalGas < totalCost else res