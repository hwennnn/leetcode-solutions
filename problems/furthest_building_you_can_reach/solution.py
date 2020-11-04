class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        n = len(heights)
        heap = []
        
        for i in range(n-1):
            d = heights[i+1] - heights[i]
            
            if d > 0:
                heapq.heappush(heap,d)
            
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            
            if bricks < 0:
                return i
        
        return n - 1
            