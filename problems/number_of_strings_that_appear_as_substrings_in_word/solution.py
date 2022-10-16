class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        
        for p in patterns:
            if p in word:
                res += 1
        
        return res