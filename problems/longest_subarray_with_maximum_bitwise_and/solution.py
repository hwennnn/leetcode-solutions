class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        mmax = max(nums)
        curr = res = 0

        for x in nums:
            if x == mmax:
                curr += 1
            else:
                curr = 0
            
            res = max(res, curr)
        
        return res
            