class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        low, high = 0, n - 1
        i = low
        
        while i <= high:
            if nums[i] == 0:
                if nums[low] != 0:
                    nums[i], nums[low] = nums[low], nums[i]
                i += 1
                low += 1
            elif nums[i] == 2:
                if nums[high] != 2:
                    nums[i], nums[high] = nums[high], nums[i]
                high -= 1
            else:
                i += 1
        