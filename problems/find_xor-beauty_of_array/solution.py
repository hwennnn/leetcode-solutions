class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        
        for x in nums:
            res ^= x
        
        return res