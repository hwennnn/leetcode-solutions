class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        m = max(candies)
        n = len(candies)
        
        for i in range(n):
            candy = candies[i] + extraCandies
            if candy >= m:
                candies[i] = True
            else:
                candies[i] = False
                

        return candies
       