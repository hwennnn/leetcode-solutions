class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = not_rob = 0
        
        for x in nums:
            rob, not_rob = not_rob + x, max(not_rob, rob)
        
        return max(rob, not_rob)