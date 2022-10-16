class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
    
        def move(h1, h2):
            value, index = heapq.heappop(h1)
            heapq.heappush(h2, (-value, index))
        
        def median():
            return float(large[0][0]) if k & 1 else (large[0][0] - small[0][0]) / 2
    
        small, large = [], []
        for i in range(k):
            heapq.heappush(small, (-nums[i], i))
        
        for _ in range(k - (k >> 1)):
            move(small, large)
        
        res = [median()]
        
        for i, x in enumerate(nums[k:]):
            if x >= large[0][0]:
                heapq.heappush(large, (x, i + k))
                if nums[i] <= large[0][0]:
                    move(large, small)
            else:
                heapq.heappush(small, (-x, i + k))
                if nums[i] >= large[0][0]:
                    move(small, large)
            
            while small and small[0][1] <= i:
                heapq.heappop(small)
            
            while large and large[0][1] <= i:
                heapq.heappop(large)
            
            res.append(median())
            
        return res