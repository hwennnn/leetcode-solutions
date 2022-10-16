from sortedcontainers import SortedList

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = defaultdict(list)

        for left, right, height in buildings:
            events[left].append((1, height))
            events[right].append((-1, height))
        
        sl = SortedList()
        sl.add(0)
        res = []
        lastHeight = 0

        for loc in sorted(events.keys()):
            for t, height in events[loc]:
                if t == 1:
                    sl.add(height)
                else:
                    sl.remove(height)
            
            currHeight = sl[-1]
            if currHeight != lastHeight:
                res.append((loc, currHeight))
            
            lastHeight = currHeight
        
        return res