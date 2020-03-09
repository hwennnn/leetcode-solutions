class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        
        l, r, n = 0, len(A)-1, len(A)
        
        while l + 1 < n and A[l + 1] > A[l]: l += 1
        while r > 0 and A[r - 1] > A[r]: r -= 1
        
        return 0 < l == r < n-1
            