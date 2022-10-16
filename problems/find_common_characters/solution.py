class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        counter = Counter(words[0])
        
        for i in range(1, n):
            counter &= Counter(words[i])
        
        res = []
        
        for k, v in counter.items():
            res += [k] * v
        
        return res