class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        
        while len(heap) >= 2:
            y, x = -heapq.heappop(heap), -heapq.heappop(heap)
            
            if x != y:
                heapq.heappush(heap, -(y - x))
        
        return -heap[0] if heap else 0