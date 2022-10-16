class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1: return "a"
        if n % 2:
            return "a"*(n-2) + "b" + "c"
        else:
            return "a"*(n-1) + "b"