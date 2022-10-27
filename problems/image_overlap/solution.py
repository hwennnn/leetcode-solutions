class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        rows, cols = len(img1), len(img1[0])
        A = [(i, j) for i in range(rows) for j in range(cols) if img1[i][j] == 1]
        B = [(i, j) for i in range(rows) for j in range(cols) if img2[i][j] == 1]
        counter = Counter((a - c, b - d) for a, b in A for c, d in B)
        
        return max(counter.values() or [0])