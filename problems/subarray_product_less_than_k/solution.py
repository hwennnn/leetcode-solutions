class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = res = 0
        c = 1
        
        for j, x in enumerate(nums):
            c *= x
            while i <= j and c >= k:
                c /= nums[i]
                i += 1
            
            res += (j - i + 1)
        
        return res