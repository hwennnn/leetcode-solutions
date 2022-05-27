class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        
        while num > 0:
            res += 1
            
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
        
        return res