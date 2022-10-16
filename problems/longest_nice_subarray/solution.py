class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1
        i = mask = 0
        
        for j, x in enumerate(nums):
            while mask & x != 0:
                mask ^= (nums[i])
                i += 1
                
            mask |= x
            res = max(res, j - i + 1)
        
        return res