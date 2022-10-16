class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        res = 0
        
        for mask in range(1, 1 << n):
            count = 0
            valid = True
            
            for j in range(n):
                if mask & (1 << j) > 0:
                    count += 1
                    
                    for k in range(n):
                        if statements[j][k] == 1 and mask & (1 << k) == 0:
                            valid = False
                            break
                        elif statements[j][k] == 0 and mask & (1 << k) > 0:
                            valid = False
                            break
            
            if valid:
                res = max(res, count)
        
        return res
        