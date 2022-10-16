class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        size = a + b + c
        A, B, C = 0, 0, 0
        res = ""
        
        for i in range(size):
            if (a >= b and a >= c and A != 2) or (B == 2 and a > 0) or (C == 2 and a > 0):
                res += "a"
                a -= 1
                A += 1
                B = 0
                C = 0
            
            elif (b >= a and b >= c and B != 2) or (A == 2 and b > 0) or (C == 2 and b > 0):
                res += "b"
                b -= 1
                B += 1
                A = 0
                C = 0
            
            elif (c >= a and c >= b and C != 2) or (A == 2 and c > 0) or (B == 2 and c > 0):
                res += "c"
                c -= 1
                C += 1
                A = 0
                B = 0
        
        return res