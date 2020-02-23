class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        
        return int(min(len(candies)/2,len(set(candies))))