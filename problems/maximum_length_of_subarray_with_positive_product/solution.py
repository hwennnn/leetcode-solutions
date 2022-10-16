class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        res = negCount = 0
        zeroPos = negPos = -1
        
        for i, x in enumerate(nums):
            if x < 0:
                negCount += 1
                if negPos == -1:
                    negPos = i
            elif x == 0:
                negCount = 0
                zeroPos = i
                negPos = -1
            
            if negCount % 2 == 0:
                res = max(res, i - zeroPos)
            else:
                res = max(res, i - negPos)
        
        return res