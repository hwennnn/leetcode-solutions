class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        texts = text.split()
        spaces = 0
        
        for i in text:
            if i == " ":
                spaces += 1
        if len(texts) == 1:
            return texts[0] + " " * spaces
            
        between = spaces // (len(texts)-1)
        leftover = spaces % (len(texts)-1)
        
        return (" " * between).join(texts) + " "*leftover