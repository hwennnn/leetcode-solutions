class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        
        for x in range(1000, 0, -1):
            if x in s and -x in s:
                return x
        
        return -1