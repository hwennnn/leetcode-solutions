class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        rows, cols = m, n
        
        for r, c in ops:
            rows = min(rows, r)
            cols = min(cols, c)
        
        return rows * cols