class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        
        A.sort()
        i = 0
        
        while A[i]<0 and i<len(A) and i<K:
            A[i] = -A[i]
            i += 1
        
        return sum(A) - (K-i)%2 * min(A) * 2