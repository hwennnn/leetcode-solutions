class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        
        def go(row, col):
            if row == rows: return col
            
            if 0 <= row < rows and 0 <= col < cols:
                if grid[row][col] == 1 and col == cols - 1: return -1
                
                elif grid[row][col] == 1 and col + 1 < cols and grid[row][col + 1] == -1: return -1
                
                elif grid[row][col] == -1 and col - 1 < 0: return -1
                
                elif grid[row][col] == -1 and col - 1 >= 0 and grid[row][col - 1] == 1: return -1
            
                return go(row + 1, col + grid[row][col])
            
            return -1

        return [go(0, j) for j in range(cols)]