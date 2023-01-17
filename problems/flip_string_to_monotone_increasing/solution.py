class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flipCount = oneCount = 0

        for x in s:
            if x == '0':
                flipCount += 1
            else:
                oneCount += 1
            
            flipCount = min(flipCount, oneCount)

        return flipCount