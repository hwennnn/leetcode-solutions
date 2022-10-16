class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        diff = sum(max(0, i - j) for i, j in transactions)
        res = 0
        
        for i, j in transactions:
            res = max(res, diff - max(0, i - j) + i)
        
        return res