class Solution:
    def findIntegers(self, n: int) -> int:
        n = int(bin(n)[2:])
        
        digits = []
        
        while n > 0:
            digits.append(n % 10)
            n //= 10
        
        digits.reverse()
        N = len(digits)
        
        @cache
        def dp(pos, tight, last):
            if pos == N:
                return 1
            
            res = 0
            limit = digits[pos] if tight else 1
            
            for digit in range(0, limit + 1):
                if digit == last == 1: continue
                    
                res += dp(pos + 1, tight and digit == digits[pos], digit)
            
            return res
        
        return dp(0, True, 0)