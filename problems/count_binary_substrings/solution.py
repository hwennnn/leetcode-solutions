class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        chunks, consecutive, res, n = [], 1, 0, len(s)
        
        for i in range(1, n):
            if s[i] == s[i - 1]:
                consecutive += 1
            else:
                chunks.append(consecutive)
                consecutive = 1
        chunks.append(consecutive)
        
        for i in range(1, len(chunks)):
            res += min(chunks[i], chunks[i - 1])
        
        return res
        