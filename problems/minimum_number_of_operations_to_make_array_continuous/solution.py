class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        res = n
        
        for i, start in enumerate(nums):
            end = n - 1 + start
            index = bisect.bisect(nums, end)
            between = index - i
            res = min(res, n - between)
        
        return res