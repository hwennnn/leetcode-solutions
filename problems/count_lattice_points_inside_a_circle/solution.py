class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        s = set()
        
        for x, y, r in circles:
            for dy in range(y - r, y + r + 1):
                for dx in range(x - r, x + r + 1):
                    dist = (dx - x) * (dx - x) + (dy - y) * (dy - y)
                    if dist <= r * r:
                        s.add((dx, dy))
        
        return len(s)