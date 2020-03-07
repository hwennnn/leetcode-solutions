class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        temp = []
        
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0: temp.append(index+1)
            
            nums[index] = -nums[index]
        return temp