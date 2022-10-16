class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)
        target = total / 2
        res = 0
        
        pq = [-x for x in nums]
        heapq.heapify(pq)
        
        while total > target:
            x = heapq.heappop(pq)
            x = (-x) / 2
            
            total -= x
            res += 1
            
            heapq.heappush(pq, -x)
        
        return res
        