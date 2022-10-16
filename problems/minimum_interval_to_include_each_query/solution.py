class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        A = sorted(intervals)[::-1]
        pq = []
        res = {}
        
        for q in sorted(queries):
            while A and A[-1][0] <= q:
                i, j = A.pop()
                
                if j >= q:
                    heapq.heappush(pq, [j - i + 1, j])
            
            while pq and pq[0][1] < q:
                heapq.heappop(pq)
            
            res[q] = pq[0][0] if pq else -1
        
        return [res[q] for q in queries]