class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        
        def go(cells):
            res = [0] * len(cells)
            for i in range(1, len(cells) - 1):
                if cells[i - 1] == cells[i + 1]:
                    res[i] = 1
                else:
                    res[i] = 0
            
            return res
        
        visited = set()
        cycle = 0
        hasCycle = False
        for _ in range(n):
            nextCells = go(cells)
            
            if tuple(nextCells) in visited: 
                hasCycle = True
                break
            else:
                visited.add(tuple(nextCells))
                cycle += 1
            
            cells = nextCells
        
        if hasCycle:
            count = n % cycle
            for _ in range(count):
                cells = go(cells)
        
        return cells
            