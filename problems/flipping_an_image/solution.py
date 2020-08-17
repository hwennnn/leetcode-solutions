class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        n = len(A)
        
        for i in range(n):
            A[i].reverse()
            
            for j in range(len(A[i])):
                A[i][j] = 0 if A[i][j] == 1 else 1
        
        return A
                