class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        lst = []
        for i in A:
            lst.append(i**2)
        
        lst.sort()
        return lst
            