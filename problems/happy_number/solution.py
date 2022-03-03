class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            if n in seen: return False
            
            seen.add(n)
            m = 0
            
            while n > 0:
                digit = n % 10
                m += digit * digit
                n //= 10
            
            n = m
            
        return True