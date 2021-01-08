class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        n1, n2 = len(word1), len(word2)
        p1 = p2 = i = j = 0
        
        while p1 < n1 and p2 < n2:
            l1, l2 = len(word1[p1]), len(word2[p2])

            if word1[p1][i] == word2[p2][j]:
                if i < l1 - 1: 
                    i += 1
                else:
                    i = 0
                    p1 += 1
                
                if j < l2 - 1:
                    j += 1
                else:
                    j = 0
                    p2 += 1
            else:
                return False
        
        return p1 == n1 and p2 == n2
                