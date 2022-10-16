class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        nStr = str(n)
        res = 0
        digits = list(map(int, digits))
        
        for i in range(1, len(nStr)):
            res += pow(len(digits), i)
        
        for i in range(len(nStr)):
            hasSameNumber = False
            
            for digit in digits:
                if digit < int(nStr[i]):
                    res += pow(len(digits), len(nStr) - i - 1)
                elif digit == int(nStr[i]):
                    hasSameNumber = True
            
            if not hasSameNumber: return res
        
        return res + 1