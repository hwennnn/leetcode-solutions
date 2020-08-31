class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        i = 0
        j = n-1
        
        while i+1 < n and A[i+1] > A[i]: i+=1
        
        while j > 0 and A[j-1] > A[j]: j-=1
        
        return i > 0 and i == j and j < n-1