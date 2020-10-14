class Solution:
    def rob(self, nums: List[int]) -> int:
        rob, not_rob = 0, 0
        
        for i in range(len(nums)):
            rob, not_rob = not_rob + nums[i], max(rob, not_rob)
        
        return max(rob, not_rob)