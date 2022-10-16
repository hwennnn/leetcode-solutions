class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        A = []
        
        for row in grid:
            A += row
        
        n = len(A)
        A.sort()
        
        for i in range(1, n):
            if (A[i] - A[i - 1]) % x != 0:
                return -1
        
        def go(target):
            count = 0
            
            for v in A:
                count += (abs(v - target)) // x
                
            return count
        
        mid = n // 2
        return go(A[mid]) if n & 1 else min(go(A[mid - 1]), go(A[mid]))