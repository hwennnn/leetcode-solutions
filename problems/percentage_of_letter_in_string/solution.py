class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)
        c = s.count(letter)
        # print(n, c)
        return int(c / n * 100)