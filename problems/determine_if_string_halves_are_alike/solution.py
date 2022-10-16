class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s) // 2
        ss = set("aeiouAEIOU")

        return sum(c in ss for c in s[:n]) == sum(c in ss for c in s[n:])