class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        o = image[sr][sc]
        
        if o == color: return image
        
        def go(x, y):
            image[x][y] = color
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and image[dx][dy] == o:
                    go(dx, dy)
        
        go(sr, sc)
        
        return image