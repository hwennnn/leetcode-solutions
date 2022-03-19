class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        
        for x, y in points:
            if len(pq) == k:
                heapq.heappushpop(pq, (-(x * x + y * y), x, y))
            else:
                heapq.heappush(pq, (-(x * x + y * y), x, y))
                
        return [[x, y] for _, x, y in pq]