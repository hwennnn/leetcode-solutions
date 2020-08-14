class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        
        out_size = len(A[0])
        in_size = len(A)
        
        ans = [[None for _ in range(in_size)] for _ in range(out_size)] 
        
        for i in range(in_size):
            for j in range(out_size):
                ans[j][i] = A[i][j]
        
        return ans
        