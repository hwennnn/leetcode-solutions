class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = [(sum(mat[i]), i) for i in range(len(mat))]
        res.sort()
        
        return [res[i][1] for i in range(k)]
        
        