class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def helper(word):
            return int("".join(str(ord(c) - ord('a')) for c in word))
        
        return helper(firstWord) + helper(secondWord) == helper(targetWord)