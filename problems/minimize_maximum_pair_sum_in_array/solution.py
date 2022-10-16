class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = []
        
        for i in range(n // 2):
            res.append(nums[i] + nums[n - i - 1])
        
        return max(res)