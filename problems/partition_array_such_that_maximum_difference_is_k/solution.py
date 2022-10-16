class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        res = 1
        mmin = mmax = nums[0]
        
        for i in range(1, n):
            if nums[i] > mmax:
                mmax = nums[i]
            
            if nums[i] < mmin:
                mmin = nums[i]
            
            if mmax - mmin > k:
                res += 1
                mmax = mmin = nums[i]
        
        return res