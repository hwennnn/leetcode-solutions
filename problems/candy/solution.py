class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        
        A = [(x, i) for i, x in enumerate(ratings)]
        A.sort()
        candies = [1] * n
        
        for x, i in A:
            current = candies[i]
            
            if i - 1 >= 0 and ratings[i - 1] > x:
                candies[i - 1] = max(candies[i - 1], current + 1)
            
            if i + 1 < n and ratings[i + 1] > x:
                candies[i + 1] = max(candies[i + 1], current + 1)
        
        return sum(candies)
        