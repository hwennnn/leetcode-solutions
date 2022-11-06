class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for i in range(N - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
      
        i = 0
        for x in nums:
            if x != 0:
                nums[i] = x
                i += 1

        for k in range(i, N):
            nums[k] = 0
        
        return nums