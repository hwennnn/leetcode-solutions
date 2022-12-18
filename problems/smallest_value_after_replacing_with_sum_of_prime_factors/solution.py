class Solution:
    def smallestValue(self, n: int) -> int:
        vis = set()
        
        while n not in vis:
            vis.add(n)
            
            k = 0
            
            for factor in range(2, n + 1):
                while n % factor == 0:
                    k += factor
                    n //= factor
            
            n = k

        return n