class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capitals = 0
        n = len(word)
        
        for x in word:
            if ord("A") <= ord(x) <= ord("Z"):
                capitals += 1
        
        return capitals == n or capitals == 0 or (capitals == 1 and ord("A") <= ord(word[0]) <= ord("Z"))