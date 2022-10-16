class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res = 0
        
        for x in words:
            if s.startswith(x):
                res += 1
        
        return res