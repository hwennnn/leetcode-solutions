class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s = res = 0
        total = sum(nums)
        
        for x in nums[:-1]:
            s += x
            total -= x
            
            if s >= total:
                res += 1
        
        return res