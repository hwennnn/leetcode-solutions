class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
    
        while len(stones) > 1:
            stones.sort()
            val1,val2 = stones[-1], stones[-2]
            val = val1 - val2 if val1 != val2 else 0
            stones = stones[:-2] + [val] if val else stones[:-2]
            
        return stones[-1] if stones else 0