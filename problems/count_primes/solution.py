class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1: return 0
        
        arr = [True] * n
        arr[0] = arr[1] = False
        
        for i in range(2, n):
            if arr[i]:
                for j in range(i * i, n, i):
                    arr[j] = False
        
        return sum(arr)