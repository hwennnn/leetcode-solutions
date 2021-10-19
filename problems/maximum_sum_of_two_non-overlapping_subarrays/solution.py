class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        for i in range(1, len(A)):
            A[i] += A[i - 1]

        res, Lmax, Mmax = A[L + M - 1], A[L - 1], A[M - 1]
        
        # window  | --- L --- | --- M --- |
        for i in range(L + M, len(A)):
            Lmax = max(Lmax, A[i - M] - A[i - L - M])
            res = max(res, Lmax + A[i] - A[i - M])
            
        # window  | --- M --- | --- L --- |
        for i in range(L + M, len(A)):
            Mmax = max(Mmax, A[i - L] - A[i - L - M])
            res = max(res, Mmax + A[i] - A[i - L])

        return res