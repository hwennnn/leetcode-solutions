class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        
        for x, y in points:
            v = (-(x * x + y * y), x, y)

            if len(pq) >= k:
                heapq.heappushpop(pq, v)
            else:
                heapq.heappush(pq, v)
        
        return [[x, y] for _, x, y in pq]