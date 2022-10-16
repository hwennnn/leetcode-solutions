class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        heap = [(-v, k) for k, v in counter.items()]
        heapq.heapify(heap)
        res = 0
        
        while heap:
            intervals = n + 1
            temp = []
            
            while heap and intervals > 0:
                v, k = heapq.heappop(heap)
                v = -v
                v -= 1
                if v > 0:
                    temp.append((-v, k))
                res += 1
                intervals -= 1
            
            for v, k in temp:
                heapq.heappush(heap, (v, k))
            
            if not heap: break
            
            res += intervals
        
        return res