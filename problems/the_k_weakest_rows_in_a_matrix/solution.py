class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        
        temp = [[sum(mat[i]),i ]for i in range(len(mat))]
        lst = sorted(temp)

        return ([i[1] for i in lst[:k]])