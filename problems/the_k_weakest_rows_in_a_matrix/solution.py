class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = [None] * len(mat)
        
        for i,r in enumerate(mat):
            arr[i] = (-sum(1 for x in r if x == 1), -i)
        
        arr.sort()
        arr.reverse()
        
        res = []
        
        for i in range(k):
            res.append(-arr[i][1])
        
        return res