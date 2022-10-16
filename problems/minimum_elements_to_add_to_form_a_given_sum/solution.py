class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        total = sum(nums)
        target = abs(goal - total)
        
        res = target // limit + (1 if target % limit else 0)
        
        return res