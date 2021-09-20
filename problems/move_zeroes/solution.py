class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroPos = 0
        
        for i, x in enumerate(nums):
            if x != 0:
                nums[i], nums[zeroPos] = nums[zeroPos], nums[i]
                zeroPos += 1