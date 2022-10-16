class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = even = 0
        
        for x in position:
            if x % 2 == 0:
                even += 1
            else:
                odd += 1
        
        return min(even, odd)