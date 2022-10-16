class Solution:
    def canBeTypedWords(self, text: str, letters: str) -> int:
        text = text.split(' ')
        ss = set(letters)
        res = len(text)
        
        for t in text:
            if set(t) & ss:
                res -= 1
        
        return res