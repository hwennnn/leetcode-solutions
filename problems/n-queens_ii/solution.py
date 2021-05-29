class Solution:
    def totalNQueens(self, n: int, diag1 = set(), diag2 = set(), cols = set(), row = 0) -> int:
        if row == n: return 1
        
        count = 0
        
        for col in range(n):
            if row+col in diag1 or row-col in diag2 or col in cols: continue
            diag1.add(row+col)
            diag2.add(row-col)
            cols.add(col)
            
            count += self.totalNQueens(n, diag1, diag2, cols, row + 1)
            
            diag1.remove(row+col)
            diag2.remove(row-col)
            cols.remove(col)
            
        return count