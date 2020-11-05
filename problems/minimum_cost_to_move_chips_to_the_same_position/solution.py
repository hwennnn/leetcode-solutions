class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = even = 0
        
        for p in position:
            if p & 1:
                odd += 1
            else:
                even += 1
        
        return min(odd, even)