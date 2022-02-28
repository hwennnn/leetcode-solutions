class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        original = image[sr][sc]
        
        if original == newColor: return image
        
        def dfs(x, y):
            image[x][y] = newColor
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and image[dx][dy] == original:
                    dfs(dx, dy)
        
        dfs(sr, sc)
        
        return image