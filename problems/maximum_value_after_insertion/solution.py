class Solution:
    def maxValue(self, word: str, x: int) -> str:
        
        if word[0] != '-':
            for i,c in enumerate(word):
                if x > int(c):
                    return word[:i] + str(x) + word[i:]
                
            return word + str(x)
        else:
            for i,c in enumerate(word):
                if i != 0 and x < int(c):
                    return word[:i] + str(x) + word[i:]
                
            return word + str(x)