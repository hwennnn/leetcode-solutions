class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(n)]
        res = 0
        
        for x, y in dig:
            grid[x][y] = 1
        
        for x1, y1, x2, y2 in artifacts:
            flag = True
            
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if grid[x][y] != 1:
                        flag = False
                        break
            
            if flag:
                res += 1
        
        return res
        