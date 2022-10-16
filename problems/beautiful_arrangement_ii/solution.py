class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = []
        
        i, j = 1, n
        
        for _ in range(n):
            if k % 2 == 0:
                res.append(i)
                i += 1
            else:
                res.append(j)
                j -= 1
            
            if k > 1:
                k -= 1
        
        return res