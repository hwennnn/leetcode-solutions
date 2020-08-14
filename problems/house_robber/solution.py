class Solution(object):
    def rob(self, nums):
        
        # if not nums:
        #     return 0
        # if len(nums) < 2:
        #     return nums[0]
        # nums[1] = max(nums[0], nums[1])
        # for i in range(2, len(nums)):
        #     nums[i] = max((nums[i-2]+nums[i]), nums[i-1])
        # return nums[-1]

        
        n = len(nums)
        ifRobbed = ifNotRobbed = 0
        
        for i in range(n):
            rob_this = ifNotRobbed + nums[i]
            
            no_rob_this = max(ifRobbed, ifNotRobbed)
            
            ifRobbed = rob_this
            
            ifNotRobbed = no_rob_this
        
        return max(ifRobbed, ifNotRobbed)
            
        