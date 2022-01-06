class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        
        for num, start, end in trips:
            events.append((start, 1, num))
            events.append((end, -1, num))
        
        events.sort()
        
        for _, t, x in events:
            if t == 1:
                capacity -= x
            else:
                capacity += x
            if capacity < 0: return False
        
        return True