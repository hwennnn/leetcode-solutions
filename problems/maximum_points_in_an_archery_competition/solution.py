class Solution:
    def maximumBobPoints(self, N: int, A: List[int]) -> List[int]:
        res = [0] * 12
        best = 0
        
        for mask in range(1 << 12):
            cand = [0] * 12
            score = used = 0
            
            for j in range(12):
                if mask & (1 << j):
                    cand[j] += A[j] + 1
                    used += A[j] + 1
                    score += j
            
            if score > best and used <= N:
                res = cand
                best = score
        
        res[0] += N - sum(res)
        
        return res