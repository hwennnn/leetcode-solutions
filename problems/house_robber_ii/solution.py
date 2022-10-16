class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        def rob_helper(start, end):
            rob = not_rob = 0
            
            for i in range(start, end):
                rob, not_rob = not_rob + nums[i], max(not_rob, rob)
            
            return max(rob, not_rob)
        
        return max(rob_helper(0, len(nums) - 1), rob_helper(1, len(nums)))