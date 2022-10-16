class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapq.heapify(heap)
        
        res = 0
        for _ in range(k):
            pile = -heapq.heappop(heap)
            res += pile
            heapq.heappush(heap, -ceil(pile / 2))
        
        return -sum(heap)
        