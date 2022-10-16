from heapq import heappop, heappush
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        i = res = 0
        
        heap = []
        
        while True:
            if i < n:
                heappush(heap, (days[i] + i, apples[i]))
            
            while heap and i >= heap[0][0]:
                heappop(heap)
                
            if heap:
                rot, apple = heappop(heap)
                res += 1
                if apple > 1:
                    heappush(heap, (rot, apple - 1))
            
            
            if not heap and i >= n: break
            
            i += 1
        
        return res