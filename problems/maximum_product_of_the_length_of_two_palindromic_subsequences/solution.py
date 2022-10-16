class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        N = 1 << n
        A = []
        
        for mask in range(1, N):
            subseq = ''
            for i in range(n):
                if (mask >> i) & 1:
                    subseq += s[i]
            
            if subseq == subseq[::-1]:
                A.append((mask, len(subseq)))
        
        A.sort(key = lambda x:-x[1])
        res = 1
        for i in range(len(A)):
            mask1, len1 = A[i]
            if len1 ** 2 < res: break
            
            for j in range(i + 1, len(A)):
                mask2, len2 = A[j]
                if mask1 & mask2 == 0 and len1 * len2 > res:
                    res = len1 * len2
                    break
        
        return res