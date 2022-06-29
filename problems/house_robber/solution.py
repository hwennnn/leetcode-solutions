class Solution:
    def rob(self, nums: List[int]) -> int:
        take = skip = 0
        
        for x in nums:
            take, skip = max(take, skip + x), max(skip, take)
            
        return take