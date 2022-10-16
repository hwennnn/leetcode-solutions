class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mp = {x:i for i, x in enumerate(nums)}
        
        for a, b in operations:
            currIndex = mp[a]
            nums[currIndex] = b
            mp[b] = currIndex
        
        return nums