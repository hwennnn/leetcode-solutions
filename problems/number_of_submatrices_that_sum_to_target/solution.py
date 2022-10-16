class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        for i in range(rows):
            for j in range(1, cols):
                matrix[i][j] += matrix[i][j - 1]
        
        res = 0
        for i in range(cols):
            for j in range(i, cols):
                mp = collections.defaultdict(int)
                curr, mp[0] = 0, 1
                
                for k in range(rows):
                    curr += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    res += mp[curr - target]
                    mp[curr] += 1
        
        return res