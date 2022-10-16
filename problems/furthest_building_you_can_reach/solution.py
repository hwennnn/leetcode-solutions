class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        
        for i in range(n - 1):
            delta = heights[i + 1] - heights[i]
            
            if delta > 0:
                heappush(heap, delta)
                if ladders > 0:
                    ladders -= 1
                else:
                    use = heappop(heap)
                    if bricks >= use:
                        bricks -= use
                    else:
                        return i
                    
        
        return n - 1