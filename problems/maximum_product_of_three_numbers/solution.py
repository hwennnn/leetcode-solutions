class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2 : return 0
        
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])