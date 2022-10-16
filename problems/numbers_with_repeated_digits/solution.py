class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        
        def findNonRepeated(n):
            digits = []

            while n > 0:
                digits.append(n % 10)
                n //= 10

            digits.reverse()

            N = len(digits)

            @cache
            def dp(pos, tight, mask):
                if pos == N:
                    return 1 if mask != 0 else 0

                limit = digits[pos] if tight else 9
                res = 0

                for i in range(0, limit + 1):
                    if mask & (1 << i) > 0: continue

                    nextTight = tight and i == digits[pos]
                    nextMask = mask if i == 0 and mask == 0 else mask ^ (1 << i)

                    res += dp(pos + 1, nextTight, nextMask)

                return res
            
            return dp(0, True, 0)
        
        return n - findNonRepeated(n)