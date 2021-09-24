class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int: 
        n = len(cardPoints)
        t = n - k
        total = sum(cardPoints)
        prefix = [0] + list(accumulate(cardPoints))
        res = float('inf')

        for i in range(t, n + 1):
            res = min(res, prefix[i] - prefix[i - t])

        return total - res
        