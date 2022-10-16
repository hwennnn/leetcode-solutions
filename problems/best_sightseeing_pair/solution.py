class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = curr = 0
        
        for v in values:
            res = max(res, curr + v)
            curr = max(curr, v) - 1
        
        return res