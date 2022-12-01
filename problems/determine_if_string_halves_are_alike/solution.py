class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        N = len(s)
        first = second = 0
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        for i in range(N):
            if s[i] in vowels:
                if i < N // 2:
                    first += 1
                else:
                    second += 1

        return first == second