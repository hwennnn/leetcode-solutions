class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        @cache
        def go(i, curr):
            if i == n and curr == target:
                return 1
            if i == n:
                return 0
            
            return go(i + 1, curr + nums[i]) + go(i + 1, curr - nums[i])
        
        return go(0, 0)