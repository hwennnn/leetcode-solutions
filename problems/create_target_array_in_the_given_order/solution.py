class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        temp = []
        
        for i in range(len(index)):
            temp.insert(index[i], nums[i])
            
        return temp