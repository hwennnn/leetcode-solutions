class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                dp[(j, nums[j] - nums[i])] = dp.get((i, nums[j] - nums[i]), 1) + 1
        
        return max(dp.values())