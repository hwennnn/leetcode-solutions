class Solution:
    def findLatestStep(self, A: List[int], m: int) -> int:
        if m == len(A): return m
        
        length = [0] * (len(A) + 2)
        res = -1
        for i, a in enumerate(A):
            left, right = length[a - 1], length[a + 1]
        
            if left == m or right == m:
                res = i
            length[a - left] = length[a + right] = left + right + 1
        
        return res