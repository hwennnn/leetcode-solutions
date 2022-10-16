class Solution:
    def reinitializePermutation(self, n: int) -> int:
        arr = [i for i in range(n)]
        desired = [i for i in range(n)]
        
        count = 0
        
        while count == 0 or arr != desired:
            tmp = [0] * n 
            
            for i in range(n):
                if i % 2 == 0:
                    tmp[i] = arr[i // 2]
                else:
                    tmp[i] = arr[n // 2 + (i-1) // 2]
            
            arr = tmp
            count += 1
            
        return count
        