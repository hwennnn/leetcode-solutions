class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        A = [False] * (n + 1)
        res = 0
        
        for x in banned:
            if x > n: continue
            A[x] = True
        
        for x in range(1, n + 1):
            if A[x]: continue
                
            if x > maxSum: break
            
            res += 1
            maxSum -= x
        
        return res