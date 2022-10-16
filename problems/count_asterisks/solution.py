class Solution:
    def countAsterisks(self, s: str) -> int:
        A = s.split('|')
        n = len(A)
        res = 0
        
        for i in range(0, n, 2):
            res += A[i].count("*")
        
        return res