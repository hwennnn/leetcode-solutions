class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = collections.deque()
        
        for x in range(rows):
            for y in range(cols):
                if mat[x][y] == 0:
                    queue.append((x, y))
                else:
                    mat[x][y] = float('inf')
        
        while queue:
            x, y = queue.popleft()
            
            for dx,dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= dx < rows and 0 <= dy < cols and mat[x][y] < mat[dx][dy]:
                    queue.append((dx, dy))
                    mat[dx][dy] = mat[x][y] + 1
        
        return mat