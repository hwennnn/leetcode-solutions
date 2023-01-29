class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        N = len(weights)
        if N == k or k == 1: return 0
        candidates = []

        for a, b in zip(weights, weights[1:]):
            candidates.append(a + b)
        
        candidates.sort()
        mmax = mmin = 0

        for i in range(k - 1):
            mmin += candidates[i]
            mmax += candidates[-i - 1]
        
        return mmax - mmin

        
        