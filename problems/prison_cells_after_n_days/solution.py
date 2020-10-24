class Solution:
    def nextDay(self, cells):
        tmp = [0] * len(cells)
        for i in range(1,len(cells) - 1):
            if (cells[i-1] == cells[i+1]):
                tmp[i] = 1
            else:
                tmp[i] = 0

        return tmp

                        
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if not cells or N <= 0: return cells
        hasCycle = False
        cycle = 0
        s = set()
        
        for i in range(N):
            nxt = self.nextDay(cells)
            if tuple(nxt) not in s:
                s.add(tuple(nxt))
                cycle += 1
            else:
                hasCycle = True
                break
            
            cells = nxt
        
        if hasCycle:
            turns = N % cycle
            for i in range(turns):
                cells = self.nextDay(cells)
        
        
        return cells