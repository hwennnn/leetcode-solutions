class Solution:
    def restoreMatrix(self, rs: List[int], cs: List[int]) -> List[List[int]]:
        r = len(rs)
        c = len(cs)
        
        lst = [[0]*c for _ in range(r)]
        
        for i in range(r):
            for j in range(c):
                
                cur = min(rs[i], cs[j])
                
                lst[i][j] = cur
                rs[i] -= cur
                cs[j] -= cur

        return lst
                