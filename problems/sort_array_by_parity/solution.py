class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        
        for j, x in enumerate(nums):
            if x % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        
        return nums
        