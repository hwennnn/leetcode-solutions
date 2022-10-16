class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flipCount = onesCount = 0
        
        for c in s:
            if c == '0':
                if onesCount == 0:
                    continue
                else:
                    flipCount += 1
            else:
                onesCount += 1
            
            if flipCount > onesCount:
                flipCount = onesCount
        
        return flipCount