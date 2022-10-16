class Solution:
    def countOrders(self, n: int) -> int:
        M = 10 ** 9 + 7
        res = 1
        
        for i in range(2, n + 1):
            res *= i * (i * 2 - 1)
            res %= M
        
        return res
        