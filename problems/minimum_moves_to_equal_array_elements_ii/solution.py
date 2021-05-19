class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res, i, j = 0, 0, n - 1
        
        while i < j:
            res += nums[j] - nums[i]
            i += 1
            j -= 1
        
        return res
        