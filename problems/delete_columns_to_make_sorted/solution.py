class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0

        for cols in zip(*strs):
            for a, b in zip(cols, cols[1:]):
                if a > b:
                    res += 1
                    break
        
        return res
