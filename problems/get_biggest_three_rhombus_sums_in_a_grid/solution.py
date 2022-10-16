class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        res = set()
        
        def isValid(pos):
            return 0 <= pos[0] < rows and 0 <= pos[1] < cols
        
        def calculateTotal(lst, size):
            top, left, right, bottom = lst
            x, y = top
            total = grid[top[0]][top[1]] + grid[bottom[0]][bottom[1]] if size > 0 else grid[top[0]][top[1]]
            
            for i in range(1, size + 1):
                l = (x + i, y - i)
                r = (x + i, y + i)
                total += (grid[l[0]][l[1]] + grid[r[0]][r[1]])
            
            if size > 1:
                x, y = bottom
                for i in range(1, size):
                    l = (x - i, y + i)
                    r = (x - i, y - i)
                    total += (grid[l[0]][l[1]] + grid[r[0]][r[1]])
            
            return total
        
        def dfs(x, y, size):
            top = (x, y)
            left = (x + size, y - size)
            right = (x + size, y + size)
            bottom = (x + (size * 2) , y) if size != 0 else top
            
            lst = [top, left, right, bottom]
            
            if all(isValid(pos) for pos in lst):
                total = calculateTotal(lst, size)
                res.add(total)
                dfs(x, y, size + 1)
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, 0)
        
        return sorted(list(res))[::-1][:3]