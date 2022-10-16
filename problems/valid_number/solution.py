class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        pointSeen = eSeen = numberSeen = False
        
        for i,x in enumerate(s):
            if x >= '0' and x <= '9':
                numberSeen = True
            elif x == '.':
                if pointSeen or eSeen: return False
                pointSeen = True
            elif x == 'e' or x == 'E':
                if eSeen or not numberSeen: return False
                eSeen = True
                numberSeen = False
            elif x == '+' or x == '-':
                if i != 0 and s[i - 1] != 'e' and s[i - 1] != 'E': return False
            else:
                return False
        
        return numberSeen
