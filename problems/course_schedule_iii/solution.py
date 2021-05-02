class Solution:
    def scheduleCourse(self, A: List[List[int]]) -> int:
        A.sort(key = lambda x:x[1])
        pq = []
        curr = 0
        
        for i, (t,l) in enumerate(A):
            curr += t
            heapq.heappush(pq, -t)
            if curr > l:
                curr += heapq.heappop(pq)
            
        return len(pq)