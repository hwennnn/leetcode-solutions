class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left, right = 0, len(nums) - 1
        i = 0
        
        while i <= right:
            if nums[i] == 0:
                if nums[left] != 0:
                    nums[left], nums[i] = nums[i], nums[left]
                
                left += 1
                i += 1
            elif nums[i] == 2:
                if nums[right] != 2:
                    nums[right], nums[i] = nums[i], nums[right]
                
                right -= 1
            else:
                i += 1