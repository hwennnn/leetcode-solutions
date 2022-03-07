class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return "".join(Counter(t) - Counter(s))