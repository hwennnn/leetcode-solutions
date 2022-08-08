class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        @cache
        def go(index):
            if index >= n:
                return True
            
            valid = False
            
            if index + 1 < n and nums[index] == nums[index + 1]:
                valid |= go(index + 2)
                
            if index + 2 < n and nums[index] == nums[index + 1] == nums[index + 2]:
                valid |= go(index + 3)
                
            if index + 2 < n and nums[index] + 1 == nums[index + 1] and nums[index + 1] + 1 == nums[index + 2]:
                valid |= go(index + 3)
            
            return valid
            
        return go(0)