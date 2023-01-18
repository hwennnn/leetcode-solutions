class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        N = len(nums)
        currMax = mmax = currMin = mmin = total = nums[0]

        for i in range(1, N):
            currMax = max(nums[i], nums[i] + currMax)
            mmax = max(mmax, currMax)
            currMin = min(nums[i], nums[i] + currMin)
            mmin = min(mmin, currMin)
            total += nums[i]
        
        return max(mmax, total - mmin) if mmax > 0 else mmax
