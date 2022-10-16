class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        A = [[1] * (i + 1) for i in range(numRows)]
        
        for row in range(2, numRows):
            for j in range(1, len(A[row]) - 1):
                A[row][j] = A[row - 1][j - 1] + A[row - 1][j]
        
        return A