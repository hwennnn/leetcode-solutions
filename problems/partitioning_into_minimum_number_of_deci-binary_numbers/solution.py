class Solution:
    def minPartitions(self, n: str) -> int:
        res = float('-inf')
        
        for c in n:
            res = max(int(c), res)    
        
        return res