class Solution:
    def scheduleCourse(self, A: List[List[int]]) -> int:
        A.sort(key = lambda x:x[1])
        pq = []
        curr = 0
        
        for t, l in A:
            curr += t
            heappush(pq, -t)
            if curr > l:
                curr += heappop(pq)
            
        return len(pq)