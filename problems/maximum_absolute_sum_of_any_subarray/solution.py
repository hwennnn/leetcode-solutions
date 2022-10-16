class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mmax = mmin = s = 0
        
        for num in nums:
            s += num
            mmax = max(mmax, s)
            mmin = min(mmin, s)

        return mmax - mmin