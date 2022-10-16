class Solution:
    def maxProductPath(self, A: List[List[int]]) -> int:
        M = 1000000007
        row, col = len(A), len(A[0])
        
        mp = [[0] * col for _ in range(row)] 
        mn = [[0] * col for _ in range(row)] 
        mp[0][0] = mn[0][0] = A[0][0]
        
        for i in range(1,col):
            mp[0][i] = A[0][i] * mp[0][i-1]
            mn[0][i] = A[0][i] * mp[0][i-1]
        
        for i in range(1,row):
            mp[i][0] = A[i][0] * mp[i-1][0]
            mn[i][0] = A[i][0] * mp[i-1][0]
            
        for i in range(1,row):
            for j in range(1,col):
                if A[i][j] > 0:
                    mp[i][j] = max(mp[i-1][j], mp[i][j-1]) * A[i][j]
                    mn[i][j] = min(mn[i-1][j], mn[i][j-1]) * A[i][j]
                else:
                    mp[i][j] = min(mn[i-1][j], mn[i][j-1]) * A[i][j]
                    mn[i][j] = max(mp[i-1][j], mp[i][j-1]) * A[i][j]
        
        res = mp[row-1][col-1]
        
        return res%M if res > -1 else -1