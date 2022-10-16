class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        
        for i in range(n // 2):
            if text[:i + 1] == text[n - i - 1:]:
                return 2 + self.longestDecomposition(text[i + 1: n - i - 1])
        
        return 0 if n == 0 else 1