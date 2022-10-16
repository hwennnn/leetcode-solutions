class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []
        
        rows, cols = len(matrix), len(matrix[0])
        res = []
        
        p_visited = [[False for _ in range(cols)] for _ in range(rows)]
        a_visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        def dfs(i, j, visited):
            visited[i][j] = True
            
            for dx,dy in ((i+1, j), (i-1, j), (i, j-1), (i, j+1)):
                if 0 <= dx < rows and 0 <= dy < cols and matrix[dx][dy] >= matrix[i][j] and not visited[dx][dy]:
                    dfs(dx, dy, visited)
        
        for i in range(rows):
            dfs(i, 0, p_visited)
            dfs(i, cols - 1, a_visited)
        
        for j in range(cols):
            dfs(0, j, p_visited)
            dfs(rows - 1, j, a_visited)
        
        for i in range(rows):
            for j in range(cols):
                if a_visited[i][j] and p_visited[i][j]:
                    res.append([i,j])

        return res