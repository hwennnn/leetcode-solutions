class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        
        for k1, v1 in counter1.items():
            if abs(counter2[k1] - v1) > 3:
                return False
        
        for k2, v2 in counter2.items():
            if abs(counter1[k2] - v2) > 3:
                return False
        
        return True