class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        lst = []
        for i in J:
            lst.append(i)
        count=0
        
        for i in S:
            if i in lst:
                count+=1
        return count
            