class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        r,c = len(matrix), len(matrix[0])
        col = [0] * c
        # calculate max col
        for i in range(c):
            col[i] = max([matrix[j][i] for j in range(r)])
        
        res = []
        for i in range(r):
            for j in range(c):
                if min(matrix[i]) == matrix[i][j] and col[j] == matrix[i][j]:
                    res.append(matrix[i][j])
                
        return res