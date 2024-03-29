class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        
        for i,x in enumerate(nums):
            if target - x in mp:
                return [mp[target - x], i]
            
            mp[x] = i