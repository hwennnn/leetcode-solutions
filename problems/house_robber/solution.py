class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = skip = 0

        for x in nums:
            rob, skip = skip + x, max(rob, skip)
        
        return max(rob, skip)