class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        start = tank = 0
        
        for end in range(n * 2):
            if tank < 0:
                start = end
                tank = 0
            
            tank += gas[end % n] - cost[end % n]
            
        return start if start < n else -1
        
        