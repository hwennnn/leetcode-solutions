class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        return word == word.lower() or word == word.upper() or word == word.capitalize()
        