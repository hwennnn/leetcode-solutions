class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for x in nums:
            if len(heap) >= k:
                heapq.heappushpop(heap, x)
            else:
                heapq.heappush(heap, x)

        return heap[0]