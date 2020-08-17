class Solution:
    def distributeCandies(self, candies: int, n: int) -> List[int]:
        
        ans = [0] * n
        
        base = 0
        
        while candies > 0:
            ans[base%n] += min(candies, base+1)
            candies -= base + 1
            base += 1
        
        return ans
            