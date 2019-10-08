class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        val = [0,0]
        
        for i in moves:
            if i == "U":
                val[1]+=1
            elif i == "D":
                val[1]-=1
            elif i == "L":
                val[0]+=1
            elif i == "R":
                val[0]-=1
        
        for i in val:
            if i != 0:
                return False
        
        return True