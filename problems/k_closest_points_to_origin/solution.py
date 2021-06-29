class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x,y in points:
            dist = (x * x + y * y)
            if len(heap) == k:
                heapq.heappushpop(heap, (-dist, x, y))
            else:
                heapq.heappush(heap, (-dist, x, y))
        
        return [[x, y] for _, x, y in heap]