class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        a = b = c = 0
        M = 10 ** 9 + 7
        
        for x in nums:
            if x == 0:
                a += a + 1
            elif x == 1:
                b += b + a
            else:
                c += c + b
                c %= M
        
        return c