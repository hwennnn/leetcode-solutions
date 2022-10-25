class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        n1, n2 = len(word1), len(word2)
        i = j = ki = kj = 0
        
        while i < n1 and j < n2:
            while ki < len(word1[i]) and kj < len(word2[j]):
                if word1[i][ki] != word2[j][kj]:
                    return False
                
                ki += 1
                kj += 1
            
            if ki == len(word1[i]):
                i += 1
                ki = 0
            
            if kj == len(word2[j]):
                j += 1
                kj = 0
        
        return i == n1 and j == n2