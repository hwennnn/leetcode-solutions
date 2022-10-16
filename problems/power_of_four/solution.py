class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>=1 and not log(n,4)%1
        