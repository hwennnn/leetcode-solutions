class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        res = 0
        
        for x in nums:
            heappush(heap, -x)
        
        for _ in range(k):
            if not heap: break
                
            x = -heappop(heap)
            
            res += x
            
            new = ceil(x / 3)
            if new > 0:
                heappush(heap, -new)
        
        return res