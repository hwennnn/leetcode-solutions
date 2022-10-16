class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def profit(a, b):
            return (a + 1) / (b + 1) - a / b
        
        heap = []
        for a,b in classes:
            heap.append((-profit(a, b), a, b))
        
        heapq.heapify(heap)
        
        for _ in range(extraStudents):
            _, a, b = heapq.heappop(heap)
            heapq.heappush(heap, (-profit(a + 1, b + 1), a + 1, b + 1))
        
        return sum(a / b for _, a, b in heap) / len(classes)