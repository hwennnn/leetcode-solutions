class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMin = mmin = currMax = mmax = total = nums[0]
        
        for i in range(1, len(nums)):
            total += nums[i]
            currMin = min(nums[i], currMin + nums[i])
            mmin = min(mmin, currMin)
            currMax = max(nums[i], currMax + nums[i])
            mmax = max(mmax, currMax)

        return max(mmax, total - mmin) if mmax > 0 else mmax