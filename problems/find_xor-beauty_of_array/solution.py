class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        N = len(nums)
        curr = 0
        res = 0
        
        for i, x in enumerate(nums):
            curr |= x
            res ^= curr & x
        
        return res