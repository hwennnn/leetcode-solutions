class Solution:
    def tribonacci(self, n: int) -> int:
        seen = [None] * (38)
        seen[0] = 0
        seen[1] = 1
        seen[2] = 1
        
        def recur(n):
            if seen[n] != None: return seen[n]
            
            result = recur(n-1) + recur(n-2) + recur(n-3)
            seen[n] = result
            
            return result
        
        return recur(n)