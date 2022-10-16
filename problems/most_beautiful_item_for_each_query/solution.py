class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        n = len(items)
        items.sort(key = lambda x : (x[0], -x[1]))
        res = []
        A = [(0, 0)]
        curr = 0

        for i, (price, beauty) in enumerate(items):
            if i > 1 and price == items[i - 1][0]: continue
                
            curr = max(curr, beauty)
            A.append((price, curr))

        for q in queries:
            index = bisect.bisect(A, (q + 1, )) - 1
            res.append(A[index][1])
            
        return res
            