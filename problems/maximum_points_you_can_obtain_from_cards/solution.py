class Solution:
    def maxScore(self, A: List[int], k: int) -> int:
        n = len(A)
        total = sum(A)
        
        size = n - k
        
        prefix = [0]
        for x in A:
            prefix.append(prefix[-1] + x)
        
        res = float('inf')
        for i in range(n - size + 1):
            res = min(res, prefix[i + size] - prefix[i])
        
        return total - res