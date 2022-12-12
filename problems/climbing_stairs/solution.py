class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def fib(k):
            if k == 1: return 1
            if k == 2: return 2

            return fib(k - 2) + fib(k - 1)
        
        return fib(n)
