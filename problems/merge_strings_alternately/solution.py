class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        
        for a, b in zip_longest(word1, word2, fillvalue=""):
            res += a + b
        
        return res