class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        res = 0
        curr = capacity
        
        for i, x in enumerate(plants):
            res += 1
            curr -= x
            
            if i + 1 < n and curr < plants[i + 1]:
                res += i + 1
                res += i + 1
                curr = capacity
        
        return res