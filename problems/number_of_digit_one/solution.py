class Solution:
    def countDigitOne(self, n: int) -> int:
        digits = []
        
        while n > 0:
            digits.append(n % 10)
            n //= 10
        
        digits.reverse()
        N = len(digits)
        
        @cache
        def dp(pos, tight, count):
            if pos == N: return count
            
            limit = digits[pos] if tight else 9
            res = 0
            
            for digit in range(0, limit + 1):
                newTight = tight and digit == digits[pos]
                newCount = count + 1 if digit == 1 else count
                
                res += dp(pos + 1, newTight, newCount)
            
            return res
        
        return dp(0, True, 0)
            