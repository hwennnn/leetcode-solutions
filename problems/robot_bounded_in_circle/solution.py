class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = i = 0
        
        for c in instructions:
            if c == "R":
                i = (i + 1) % 4
            elif c == "L":
                i = (i + 3) % 4
            else:
                x, y = x + d[i][0], y + d[i][1]
        
        return (x, y) == (0, 0) or i > 0