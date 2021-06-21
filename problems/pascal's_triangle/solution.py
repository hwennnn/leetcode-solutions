class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[0] * (i + 1) for i in range(numRows)]
        
        for i, row in enumerate(res):
            row[0] = row[-1] = 1
            
            for j in range(1, len(row) - 1):
                left = res[i - 1][j - 1]
                right = res[i - 1][j]
                
                row[j] = left + right
            
        return res