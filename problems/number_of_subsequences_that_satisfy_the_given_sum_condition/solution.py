class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        M = 10 ** 9 + 7
        res = 0
        nums.sort()

        for i, x in enumerate(nums):
            index = bisect.bisect_right(nums, target - x) - 1
            
            if index >= i and x + nums[index] <= target:
                diff = index - i
                res += pow(2, diff, M)
        
        return res % M