class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [(left, -height, right) for left, right, height in buildings]
        events += list(set((right, 0, 0) for _, right, _ in buildings))
        events.sort()
        
        res = [[0, 0]]
        heap = [(0, float('inf'))]
        
        for pos, height, right in events:
            
            while heap[0][1] <= pos:
                heapq.heappop(heap)
                
            if height != 0:
                heapq.heappush(heap, (height, right))
            
            if res[-1][1] != -heap[0][0]:
                res += [[pos, -heap[0][0]]]
                
        
        return res[1:]