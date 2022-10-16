class Solution:
    def countTexts(self, A: str) -> int:
        n = len(A)
        M = 10 ** 9 + 7
        
        @cache
        def go(i):
            if i == n: return 1
            
            res = go(i + 1)
            z = 4 if A[i] in "79" else 3

            for k in range(i + 1, min(n, i + z)):
                if A[k] == A[i]:
                    res += go(k + 1)
                else:
                    break

                
            return res % M
        
        return go(0)
                
            
            