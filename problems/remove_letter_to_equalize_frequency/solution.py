class Solution:
    def equalFrequency(self, word: str) -> bool:
        N = len(word)
        
        for i in range(N):
            newWord = word[:i] + word[i + 1:]
            vals = list(Counter(newWord).values())
            
            first = vals[0]
            if all(v == first for v in vals):
                return True
        
        return False