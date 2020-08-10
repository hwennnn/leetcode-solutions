class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        n = len(s)
        temp = [None] * n
        
        for i in range(n):
            temp[indices[i]] = s[i]
            
        return "".join(temp)