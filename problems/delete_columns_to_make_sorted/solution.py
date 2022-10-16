class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        res = 0
        
        for j in range(n):
            for c1, c2 in zip(strs, strs[1:]):
                if c1[j] > c2[j]:
                    res += 1
                    break
        
        return res