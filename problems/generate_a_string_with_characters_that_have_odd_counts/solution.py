class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1: return "a"
        first = "a"
        second = "b"
        
        if n % 2 == 0:
            return first*(n-1) + second*1
        else:
            return first*n