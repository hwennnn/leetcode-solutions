class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        if n < 2: return 0
        s0 = []
        s1 = []
        s2 = []
        s0.append(0)
        s1.append(-prices[0])
        s2.append(float('-inf'))
        
        for i in range(1,n):
            s0.append(max(s0[i - 1], s2[i - 1]))
            s1.append(max(s1[i - 1], s0[i - 1] - prices[i]))
            s2.append(prices[i] + s1[i - 1])
            
        
        
        return max(s0[n - 1], s2[n - 1])