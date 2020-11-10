class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        res = []
        
        for i in range(n):
            tmp = []
            for j in reversed(A[i]):
                tmp.append(j ^ 1)
            
            res.append(tmp)
            
        return res