class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        heap = [-x for x in target]
        heapify(heap)
        
        while True:
            x = -heappop(heap)
            total -= x
            
            if x == 1 or total == 1: return True
            
            if x < total or total == 0 or x % total == 0: return False
            
            x %= total
            total += x
            
            heappush(heap, -x)