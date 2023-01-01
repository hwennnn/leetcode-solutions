class Solution:
    def countDigits(self, num: int) -> int:
        digits = [int(x) for x in str(num)]
        res = 0
        
        for digit in digits:
            if num % digit == 0:
                res += 1
        
        return res