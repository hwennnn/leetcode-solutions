class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        
        while n > 1:
            if n%2:
                res += int((n-1) / 2)
                n = int((n-1) / 2 + 1)
            else:
                res += n//2
                n //= 2
        
        return res