class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        M = 10 ** 9 + 7
        heap = []
        res = currSpeed = 0
        
        for e, s in sorted(zip(efficiency, speed), reverse = 1):
            currSpeed += s
            heappush(heap, s)
            
            if len(heap) > k:
                currSpeed -= heappop(heap)
            
            res = max(res, e * currSpeed)
            
        return res % M
        