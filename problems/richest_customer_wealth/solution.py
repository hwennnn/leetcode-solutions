class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = float('-inf')
        
        for a in accounts:
            res = max(res, sum(a))
        
        return res