class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        heap = []
        
        for start, end in flowers:
            heapq.heappush(heap, (start, 1))
            heapq.heappush(heap, (end + 1, -1))
        
        query = [(x, i) for i, x in enumerate(persons)]
        query.sort()
        n = len(query)
        queryIndex = 0
        ans = [0] * n
        
        curr = 0
        while queryIndex < n and heap:
            while heap and heap[0][0] <= query[queryIndex][0]:
                x, inc = heapq.heappop(heap)
                if inc == -1:
                    curr -= 1
                else:
                    curr += 1
            
            x, i = query[queryIndex]
            ans[i] = curr
            queryIndex += 1
        
        return ans