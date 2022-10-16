class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        
        for i, x in enumerate(nums):
            index = abs(x) - 1
            
            if nums[index] < 0: res.append(index + 1)
            
            nums[index] = -nums[index]
        
        return res