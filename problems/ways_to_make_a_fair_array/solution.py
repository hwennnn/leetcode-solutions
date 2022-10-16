class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        ro = re = 0
        for i,x in enumerate(nums):
            if i & 1: ro += x
            else: re += x
        
        lo = le = res = 0
        for i,x in enumerate(nums):
            if i & 1: ro -= x
            else: re -= x
            
            res += (lo + re) == (le + ro)
            
            if i & 1: lo += x
            else: le += x
        
        return res