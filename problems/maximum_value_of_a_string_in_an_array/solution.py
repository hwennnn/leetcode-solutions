class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = 0
        
        for x in strs:
            digitCount = 0

            for c in x:
                if c.isdigit():
                    digitCount += 1
            
            if digitCount == len(x):
                res = max(res, int(x))
            else:
                res = max(res, len(x))
            
        return res