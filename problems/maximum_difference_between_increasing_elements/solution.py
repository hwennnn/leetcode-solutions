class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        res = -1
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    res = max(res, nums[j] - nums[i])
        
        return res