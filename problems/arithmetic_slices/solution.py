class Solution:
    def numberOfArithmeticSlices(self, A: List[int]):
        n = len(A)
        curr = res = 0
        
        for i in range(2, n):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                curr += 1
                res += curr
            else:
                curr = 0
        
        return res