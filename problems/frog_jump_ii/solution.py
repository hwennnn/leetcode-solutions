class Solution:
    def maxJump(self, stones: List[int]) -> int:
        N = len(stones)
        res = stones[1] - stones[0]
        
        for i in range(2, N):
            res = max(res, stones[i] - stones[i - 2])
        
        return res