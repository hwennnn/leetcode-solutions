class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def rotate(mat):
            return [list(row)[::-1] for row in zip(*mat)]
        
        for _ in range(4):
            if mat == target: return True
            mat = rotate(mat)
        
        return False