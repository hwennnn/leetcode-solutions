class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s) // 2
        
        def count(s):
            return sum(1 for c in s if c in "aeiouAEIOU")
        
        return count(s[:n]) == count(s[n:])