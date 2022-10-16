class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        def numberToBase(n, b):
            digits = []
            
            while n:
                digits.append(n % b)
                n //= b
                
            return "".join(map(str, digits[::-1]))
        
        for k in range(2, n - 2 + 1):
            s = numberToBase(n, k)
            
            if s != s[::-1]:
                return False
            
        return True