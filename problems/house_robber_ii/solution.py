class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob0(nums):
            n = len(nums)
            ifRobbed = ifNotRobbed = 0
            
            for i in range(n-1):
                rob_this = ifNotRobbed + nums[i]
                
                dont_rob_this = max(ifRobbed, ifNotRobbed)
                
                ifRobbed = rob_this
                
                ifNotRobbed = dont_rob_this
                
            return max(ifRobbed, ifNotRobbed)
        
        
        def rob1(nums):
            n = len(nums)
            ifRobbed = ifNotRobbed = 0
            
            for i in range(1,n):
                rob_this = ifNotRobbed + nums[i]
                
                dont_rob_this = max(ifRobbed, ifNotRobbed)
                
                ifRobbed = rob_this
                
                ifNotRobbed = dont_rob_this
                
            return max(ifRobbed, ifNotRobbed)
                
        
        if len(nums) == 1: return nums[0]
        
        return max(rob0(nums), rob1(nums))