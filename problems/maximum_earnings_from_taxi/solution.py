class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        heap = []
        
        for index, (start, end, profit) in enumerate(rides):
            heap.append((start, 1, index))
        
        heapq.heapify(heap)
        
        curr_max = 0
        while len(heap) > 0:
            curr, t, x = heapq.heappop(heap)
            
            if t == 1:
                end = rides[x][1]
                heapq.heappush(heap, (end, -1, curr_max + end - curr + rides[x][2]))
            else:
                curr_max = max(curr_max, x)
                
        return curr_max