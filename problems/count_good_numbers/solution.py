class Solution:
    def countGoodNumbers(self, n: int) -> int:
        M = 10 ** 9 + 7
        even = (n + 1) // 2
        odd = n // 2
        
        def ipower(base, exp):
            if exp == 0: return 1
            
            ans = ipower(base, exp // 2)
            
            if exp % 2 == 0:
                return (ans * ans) % M
            else:
                return (base * ans * ans) % M
            
        return (ipower(5, even) * ipower(4, odd)) % M
        
        