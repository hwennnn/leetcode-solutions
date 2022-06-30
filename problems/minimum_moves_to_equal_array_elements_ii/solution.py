class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        mid = nums[n // 2]
        res = 0
        
        for x in nums:
            res += abs(mid - x)
        
        return res