class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        A = []
        inter = 2 if intLength % 2 == 0 else 1
        outer = (intLength - inter) // 2
        A = []
        
        if intLength <= 4:
            for x in range(10 ** (intLength - 1), 10 ** (intLength)):
                if str(x) == str(x)[::-1]:
                    A.append(str(x))
        
        def solve(x):
            if intLength <= 4:
                if x >= len(A): return -1
                return A[x]
            
            outIndex = x // 10
            out = 10 ** (outer - 1) + outIndex
            
            modIndex = x % 10
            
            res = str(out) + str(modIndex) * inter + str(out)[::-1]

            if len(res) != intLength: return -1
            
            return res

        res = []
        for q in queries:
            q -= 1
            res.append(solve(q))
        
        return res