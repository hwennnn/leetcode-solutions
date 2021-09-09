class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()
        
        res = m = c = 0
        
        for i in range(n - 1, -1, -1):
            m += c + satisfaction[i]
            c += satisfaction[i]
            res = max(res, m)
        
        return res