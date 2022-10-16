class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        
        for mat in matrix:
            for m in mat:
                if len(heap) == k:
                    heappushpop(heap, -m)
                else:
                    heappush(heap, -m)

        return -heap[0]