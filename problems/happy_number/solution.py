class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            count = 0
            while n > 0:
                count += (n % 10) * (n % 10)
                n //= 10
            n = count

        return n == 1