class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        
        @cache
        def go(i, j):
            if i == n1 and j == n2: return 0
            elif i == n1: return n2 - j
            elif j == n2: return n1 - i
            
            if word1[i] == word2[j]:
                return go(i + 1, j + 1)
            else:
                return 1 + min(go(i + 1, j + 1), go(i + 1, j), go(i, j + 1))
        
        return go(0, 0)
            