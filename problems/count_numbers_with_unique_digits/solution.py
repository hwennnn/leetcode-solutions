class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        
        n = (10 ** n) - 1
        digits = []
        
        while n > 0:
            digits.append(n % 10)
            n //= 10
        
        digits.reverse()
        N = len(digits)
        
        @cache
        def dp(pos, tight, mask):
            if pos == N:
                return 1
            
            limit = digits[pos] if tight else 9
            res = 0
            
            for i in range(0, limit + 1):
                if mask & (1 << i) > 0: continue
                    
                nextTight = tight and i == digits[pos]
                nextMask = mask if i == 0 and mask == 0 else mask ^ (1 << i)
                
                res += dp(pos + 1, nextTight, nextMask)
            
            return res
        
        return dp(0, True, 0)