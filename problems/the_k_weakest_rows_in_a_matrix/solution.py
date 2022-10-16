class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        
        def countSoldier(row):
            left, right = 0, len(row)
            
            while left < right:
                mid = left + (right - left) // 2
                
                if row[mid] == 1:
                    left = mid + 1
                else:
                    right = mid
            
            return left
        
        for index, row in enumerate(mat):
            curr = (-countSoldier(row), -index)
            if len(heap) == k:
                heapq.heappushpop(heap, curr)
            else:
                heapq.heappush(heap, curr)
        
        res = []
        
        for _ in range(k):
            _, index = heapq.heappop(heap)
            res.append(-index)
        
        return res[::-1]