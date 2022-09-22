class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        
        @cache
        def go(index):
            if index == N: return True
            
            res = False
            
            if index + 1 < N and nums[index] == nums[index + 1]:
                res |= go(index + 2)
            
            if index + 2 < N and nums[index] == nums[index + 1] == nums[index + 2]:
                res |= go(index + 3)
                
            if index + 2 < N and nums[index] + 1 == nums[index + 1] and nums[index + 1] + 1 == nums[index + 2]:
                res |= go(index + 3)
            
            return res
        
        return go(0)