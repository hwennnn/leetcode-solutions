class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @cache
        def go(i, j):
            if i == j: return 1
            if i > j: return 0
            
            return 2 + go(i + 1, j - 1) if s[i] == s[j] else max(go(i + 1, j), go(i, j - 1))
        
        return go(0, len(s) - 1)