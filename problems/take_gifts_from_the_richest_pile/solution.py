class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        pq = [-x for x in gifts]
        heapq.heapify(pq)
        
        for _ in range(k):
            x = -heappop(pq)
            
            sq = int(math.sqrt(x))
            heappush(pq, -sq)
        
        return -sum(pq)