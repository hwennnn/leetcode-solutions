class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1 = Counter(words1)
        c2 = Counter(words2)
        res = 0
        
        for k in c1:
            if c1[k] == c2[k] == 1:
                res += 1
        
        return res