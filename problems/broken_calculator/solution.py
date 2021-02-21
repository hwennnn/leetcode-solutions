class Solution:
    def brokenCalc(self, X: int, Y: int):
        res = 0
        
        while Y > X:
            Y = Y // 2 if Y & 1 == 0 else Y + 1
            res += 1
                
        return res + X - Y