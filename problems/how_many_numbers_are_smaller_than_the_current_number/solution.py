class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        temp = {}
        
        arr = sorted(nums)
        
        for i in reversed(range(len(nums))):
            temp[arr[i]] = i
            
        
        return [temp[i] for i in nums]