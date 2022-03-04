class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        A = [[0.0] * col for col in range(1, query_row + 2)]
        A[0][0] = poured
        
        for i in range(query_row):
            for j in range(len(A[i])):
                if A[i][j] > 1:
                    half = (A[i][j] - 1) / 2
                    A[i + 1][j] += half
                    A[i + 1][j + 1] += half
                    A[i][j] = 1
                    
        res = A[query_row][query_glass]
        return res if res < 1 else 1