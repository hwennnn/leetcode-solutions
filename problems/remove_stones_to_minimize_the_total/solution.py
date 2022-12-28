class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-x for x in piles]
        heapify(heap)

        for _ in range(k):
            x = -heappop(heap)
            x = ceil(x / 2)

            heappush(heap, -x)
            
        return sum(-x for x in heap)