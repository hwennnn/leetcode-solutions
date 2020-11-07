class Solution:
    def numberOfSteps (self, num: int) -> int:
        res = 0
        while num != 0:
            if num & 1:
                num -= 1
            else:
                num //= 2
        
            res += 1
        
        return res