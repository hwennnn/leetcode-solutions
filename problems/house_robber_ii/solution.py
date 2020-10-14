class Solution:
    
    def rob1(self, nums, start, end):
        rob, not_rob = 0, 0
        for i in range(start, end):
            rob, not_rob = nums[i] + not_rob, max(rob, not_rob)
        
        return max(rob, not_rob)
            
        
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        return max(self.rob1(nums, 0, n-1), self.rob1(nums, 1, n))