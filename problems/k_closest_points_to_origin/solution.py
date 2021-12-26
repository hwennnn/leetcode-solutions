class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x, y in points:
            p = -(x * x + y * y)
            if len(heap) < k:
                heapq.heappush(heap, (p, x, y))
            else:
                heapq.heappushpop(heap, (p, x, y))
        
        return [[x, y] for _, x, y in heap]