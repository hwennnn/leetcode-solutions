class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        C = collections.Counter(arr)
        res = -1
        for c in C:
            if c == C[c]:
                res = max(res, c)
        
        return res