class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        inc = [1] * n
        
        for i in range(1, n):
            if prices[i - 1] - prices[i] == 1:
                inc[i] = inc[i - 1] + 1
        
        return sum(inc)