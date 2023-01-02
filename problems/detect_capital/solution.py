class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        def isCap(x):
            return ord("A") <= ord(x) <= ord("Z")
        
        N = len(word)
        cap = 0
        for x in word:
            if isCap(x):
                cap += 1
        
        return cap == N or cap == 0 or (cap == 1 and isCap(word[0]))