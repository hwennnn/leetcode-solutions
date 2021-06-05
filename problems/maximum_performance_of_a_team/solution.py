class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        heap = []
        res = ssum = 0
        
        for e, s in sorted(zip(efficiency, speed), reverse = True):
            heapq.heappush(heap, s)    
            ssum += s
            
            if len(heap) > k:
                ssum -= heapq.heappop(heap)
            
            res = max(res, e * ssum)
        
        return res % (10 ** 9 + 7)