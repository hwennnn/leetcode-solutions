class Solution:
    def minimumDeviation(self, A):
        pq = []
        for a in A:
            heapq.heappush(pq, -a * 2 if a % 2 else -a)
        res = float('inf')
        mi = -max(pq)
        while len(pq) == len(A):
            a = -heapq.heappop(pq)
            res = min(res, a - mi)
            if a % 2 == 0:
                mi = min(mi, a // 2)
                heapq.heappush(pq, -a // 2)
        return res
        