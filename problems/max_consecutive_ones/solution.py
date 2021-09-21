class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = ones = 0
        
        for x in nums:
            if x == 0:
                ones = 0
            else:
                ones += 1
        
            res = max(res, ones)
        
        return res