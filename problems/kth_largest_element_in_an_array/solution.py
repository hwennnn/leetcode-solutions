class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for x in nums:
            if len(heap) == k:
                heappushpop(heap, x)
            else:
                heappush(heap, x)
        
        return heappop(heap)