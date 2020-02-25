class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
        n = len(A)
        if n <= 2: return True
        
        increase = False
        decrease = False
        
        for i in range(1,n):
            if A[i-1] > A[i]:
                increase = True
                
            if A[i-1] < A[i]:
                decrease = True
                
            if increase and decrease:
                return False
            
        return True
                
            