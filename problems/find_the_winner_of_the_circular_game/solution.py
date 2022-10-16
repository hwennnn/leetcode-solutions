class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        A = [i for i in range(1, n + 1)]
        
        i = (0 + k - 1) % len(A)
        
        while len(A) > 1:
            A.pop(i)   
            i = (((i + k) % len(A) ) - 1) % len(A)
        
        return A[0]