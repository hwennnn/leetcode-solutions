class Solution:
    def prisonAfterNDays(self, cells: List[int], days: int) -> List[int]:
        
        def g(cells):
            masks = 0
            
            for cell, occupied in enumerate(cells):
                if occupied:
                    masks |= (1 << cell)
            
            return masks
        
        def transform(cells):
            new_cells = [0] * 8
            
            for i in range(1, 7):
                if cells[i - 1] == cells[i + 1]:
                    new_cells[i] = 1
            
            return new_cells
        
        original = cells[:]
        seen = set()
        cycle = 0
        hasCycle = False
        
        for _ in range(days):
            next_cells = transform(cells)
            masks = g(next_cells)
            
            if masks in seen:
                hasCycle = True
                break
            else:
                seen.add(masks)
                cycle += 1
            
            cells = next_cells
        
        if hasCycle:
            count = days % cycle
            
            for _ in range(count):
                cells = transform(cells)
            
        return cells