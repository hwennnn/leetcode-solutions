class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        prev = nums[-1]
        
        for i in range(n - 2, -1, -1):
            if nums[i] > prev:
                sections = ceil(nums[i] / prev)
                res += sections - 1
                prev = nums[i] // sections
            
            else:
                prev = nums[i]
            
        return res