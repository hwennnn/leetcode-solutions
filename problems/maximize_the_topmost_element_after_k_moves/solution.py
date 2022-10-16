class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        if k == 0: return nums[0]
        
        if k == 1: return -1 if n == 1 else nums[1]
        
        if n == 1: return -1 if k & 1 else nums[0]
        
        mmax = max(nums[:min(n, k - 1)])
        
        if k < n:
            mmax = max(mmax, nums[k])
        
        return mmax