class Solution:
    def minOperations(self, n: int) -> int:
        arr = [(2 * i) + 1 for i in range(n)]
        t = sum(arr) // n
        
        res = 0
        
        for num in arr:
            res += abs(t - num)
        
        return res // 2