class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        M = 10 ** 9 + 7
        pq = [x for x in nums]
        heapq.heapify(pq)
        
        while k > 0:
            x = heapq.heappop(pq) + 1
            heapq.heappush(pq, x)
            k -= 1
        
        x = 1
        
        for y in pq:
            x *= y
            x %= M

        return x
        