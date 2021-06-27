class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [-1] * n

        for _, index in sorted((rating, index) for index,rating in enumerate(ratings)):
            current = 1
            
            if index - 1 >= 0 and ratings[index] > ratings[index - 1]:
                current = max(current, res[index - 1] + 1)
            
            if index + 1 < n and ratings[index] > ratings[index + 1]:
                current = max(current, res[index + 1] + 1)
            
            res[index] = current
        
        return sum(res)