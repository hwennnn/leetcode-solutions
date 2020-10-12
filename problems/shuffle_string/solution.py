class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [None] * len(s)
        
        for idx,x in enumerate(indices):
            res[x] = s[idx]
        
        return "".join(res)
            