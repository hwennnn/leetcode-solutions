class Solution:
    def rotatedDigits(self, n: int) -> int:
        digits = []
        
        while n > 0:
            digits.append(n % 10)
            n //= 10
        
        digits.reverse()
        
        N = len(digits)
        
        rotations = {0:0, 1:1, 8:8, 2:5, 5:2, 6:9, 9:6}
        
        @cache
        def dp(pos, tight, rotated):
            if pos == N:
                return 1 if rotated else 0
            
            limit = digits[pos] if tight else 9
            res = 0
            
            for digit in range(0, limit + 1):
                if digit not in rotations: continue
                
                nextTight = tight and digit == digits[pos]
                nextRotated = rotated or rotations[digit] != digit
                
                res += dp(pos + 1, nextTight, nextRotated)    
            
            return res
        
        return dp(0, True, False)