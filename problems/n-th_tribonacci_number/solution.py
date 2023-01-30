class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1

        for _ in range(n - 2):
            a, b, c = b, c, a + b + c
        
        return c if n != 0 else 0