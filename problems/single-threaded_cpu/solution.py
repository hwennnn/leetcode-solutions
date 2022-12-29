class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        N = len(tasks)
        A = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]
        A.sort()

        t = A[0][0]
        i = 0
        heap = []
        res = []

        while len(res) < N:
            while i < N and A[i][0] <= t:
                heappush(heap, (A[i][1], A[i][2]))
                i += 1
            
            if heap:
                time, taskId = heappop(heap)
                t += time
                res.append(taskId)
            elif i < N:
                t = A[i][0]

        return res