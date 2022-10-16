class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        def findZeroes(n):
            return str(n).count("0") > 0
        
        a, b = 1, n - 1
        
        while findZeroes(a) or findZeroes(b):
            if findZeroes(a):
                a += 1
                b -= 1
            if findZeroes(b):
                a += 1
                b -= 1
        
        return [a,b]
            
        