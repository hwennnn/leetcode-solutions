class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        M = 10 ** 9 + 7
        res = []
        P = []
        
        curr = 0
        while 2 ** curr <= n:
            P.append(2 ** curr)
            curr += 1

        A = []
        curr = n
        for p in P[::-1]:
            if curr >= p:
                A.append(p)
                curr -= p
        
        A.append(1)
        A.reverse()
        
        for i in range(1, len(A)):
            A[i] *= A[i - 1]

        for left, right in queries:
            x = A[right + 1] // A[left]
            res.append(x % M)
        
        return res
        
        