class Solution:
    def distributeCandies(self, candies: int, n: int) -> List[int]:
        t = i = 0
        res = [0] * n
        
        while candies > 0:
            t += 1
            give = min(t, candies)
            candies -= give
            res[i] += give
            
            i = (i + 1) % n
            
        return res