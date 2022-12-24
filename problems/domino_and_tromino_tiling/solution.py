class Solution:
    def numTilings(self, N):
        a, b, c = 0, 1, 1

        for i in range(N - 1): 
            a, b, c = b, c, (c + c + a) % (10 ** 9 + 7)
            
        return c