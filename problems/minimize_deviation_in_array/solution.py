class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        
        for x in nums:
            heapq.heappush(heap, -x if x % 2 == 0 else -x * 2)
        
        mmin = -max(heap)
        res = float('inf')
        
        while len(heap) == len(nums):
            x = -heapq.heappop(heap)
            res = min(res, x - mmin)
            
            if x % 2 == 0:
                mmin = min(mmin, x // 2)
                heapq.heappush(heap, -x // 2)
        
        return res