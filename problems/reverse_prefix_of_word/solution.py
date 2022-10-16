class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = -1
        
        for i,x in enumerate(word):
            if ch == x:
                index = i
                break
        
        if index == -1: return word
        return word[:index + 1][::-1] + word[index + 1:]