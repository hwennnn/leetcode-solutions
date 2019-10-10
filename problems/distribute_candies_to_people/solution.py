class Solution(object):
    def distributeCandies(self, candies, n):
        res = [0] * n
        i = 0
        while candies > 0:
            res[i % n] += min(candies, i + 1)
            candies -= i + 1
            i += 1
        return res