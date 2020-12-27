class Solution:
    def replaceElements(self, A: List[int]) -> List[int]:
        mx = -1
        
        for i in range(len(A)-1, -1, -1):
            A[i],mx = mx, max(A[i], mx)
        
        return A