class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pq = []

        for i, num in enumerate(arr):
            d = abs(num - x)
            if len(pq) == k:
                heappushpop(pq, (-d, -i))
            else:
                heappush(pq, (-d, -i))
        
        res = []

        while pq:
            d, index = heappop(pq)
            index = -index
            res.append(arr[index])

        return sorted(res)
            