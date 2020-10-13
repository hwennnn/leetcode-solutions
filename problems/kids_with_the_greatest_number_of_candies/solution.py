class Solution:
    def kidsWithCandies(self, candies: List[int], ec: int) -> List[bool]:
        m = max(candies)
        
        res = []
        
        for i, c in enumerate(candies):
            res.append(c+ec >= m)
        
        return res
            