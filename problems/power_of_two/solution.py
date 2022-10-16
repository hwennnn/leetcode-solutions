class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        while n >= 2:
            # print(n)
            n /= 2
        # print(n)
        return n == 1