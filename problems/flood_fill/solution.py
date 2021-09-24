class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor: return image
        
        rows, cols = len(image), len(image[0])

        def dfs(x, y, color):
            image[x][y] = newColor
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and image[dx][dy] == color:
                    dfs(dx, dy, color)
        
        dfs(sr, sc, image[sr][sc])
        
        return image