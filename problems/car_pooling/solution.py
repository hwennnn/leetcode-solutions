class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        queue = []
        
        for num, start, end in trips:
            queue.append((start, num))
            queue.append((end, -num))
        
        queue.sort()
        
        for _, num in queue:
            capacity -= num
            
            if capacity < 0: return False
        
        return True