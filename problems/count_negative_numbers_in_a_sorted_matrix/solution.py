class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        return len([num for nums in grid for num in nums if num < 0 ])