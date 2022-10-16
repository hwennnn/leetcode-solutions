class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = float('inf')
        last = {}
        
        for j, x in enumerate(cards):
            if x in last:
                res = min(res, j - last[x] + 1)
                
            last[x] = j
        
        
        return -1 if res == float('inf') else res