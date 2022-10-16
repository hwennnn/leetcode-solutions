class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.split()
        text.sort(key = len)
        
        for i in range(len(text)):
            if i == 0:
                text[i] = text[i].capitalize()
            else:
                text[i] = text[i].lower()
                
        return " ".join(text)