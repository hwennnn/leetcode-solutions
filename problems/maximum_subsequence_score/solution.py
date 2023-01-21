class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        N = len(nums1)
        A = sorted([(x, mmin) for x, mmin in zip(nums1, nums2)], key = lambda x : -x[1])
        heap = []
        res = 0
        total = 0
        
        for x, mmin in A:
            heappush(heap, x)
            total += x
            
            if len(heap) > k:
                total -= heappop(heap)
            
            if len(heap) == k:
                res = max(res, mmin * total)
        
        return res