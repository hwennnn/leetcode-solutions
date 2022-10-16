class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        A = list(range(1, n + 1))
        res = []
        
        def backtrack(i, curr):
            if len(curr) == k:
                res.append(curr)
                return
            
            for j in range(i, len(A)):
                backtrack(j + 1, curr + [A[j]])
        
        backtrack(0, [])
        return res