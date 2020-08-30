class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        firstNegative = -1
        zeroPosition = -1
        res = 0
        neg = 0
        
        for i,x in enumerate(nums):
            if x < 0:
                neg += 1
                if firstNegative == -1:
                    firstNegative = i
            
            if x == 0:
                firstNegative = -1
                zeroPosition = i
                neg = 0
            
            else:
                if neg % 2 == 0:
                    res = max(res, i - zeroPosition)
                else:
                    res = max(res, i - firstNegative)
        
        return res