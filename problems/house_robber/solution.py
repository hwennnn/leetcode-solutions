class Solution:
    def rob(self, nums: List[int]) -> int:
        current = skipped = prev = 0
        
        for x in nums:
            current = max(prev, skipped + x)
            skipped, prev = prev, current
        
        return current