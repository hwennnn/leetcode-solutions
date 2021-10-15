class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        s0 = [0]
        s1 = [-prices[0]]
        s2 = [float('-inf')]
        
        for i in range(1, n):
            s0.append(max(s0[i - 1], s2[i - 1]))
            s1.append(max(s1[i - 1], s0[i - 1] - prices[i]))
            s2.append(prices[i] + s1[i - 1])
        
        return max(s0[-1], s2[-1])