class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        
        for i, x in enumerate(nums):
            x = abs(x) - 1
            nums[x] = -abs(nums[x])
        
        for i, x in enumerate(nums):
            if x > 0:
                res.append(i + 1)
        
        return res
        
        