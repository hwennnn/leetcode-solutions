class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rows, self.cols = len(matrix), len(matrix[0])
        
        self.prefix = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        
        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                self.prefix[i][j] += matrix[i - 1][j - 1] 
        
        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                self.prefix[i][j] += self.prefix[i][j - 1]
        
        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                self.prefix[i][j] += self.prefix[i - 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = self.prefix[row2 + 1][col1] - self.prefix[row1][col1]
        right = self.prefix[row2 + 1][col2 + 1] - self.prefix[row1][col2 + 1]

        return right - left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)