class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        s = 0
        
        for i, x in enumerate(nums):
            total -= x
            
            if s == total:
                return i
            
            s += x

            
        return -1