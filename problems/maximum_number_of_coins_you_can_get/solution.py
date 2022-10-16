class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        i = 0
        j = n-1
        res = 0
        rounds = n//3
        
        while i < rounds:
            res += piles[j-1]
            i+=1
            j-=2
        
        return res