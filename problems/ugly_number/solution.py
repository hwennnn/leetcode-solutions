class Solution:
    def isUgly(self, n: int) -> bool:
        while n % 2 == 0 and n: n //= 2
        while n % 3 == 0 and n: n //= 3
        while n % 4 == 0 and n: n //= 4
        while n % 5 == 0 and n: n //= 5
        
        return n == 1