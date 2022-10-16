class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        n = len(text)
        res = []
        
        for i in range(2, n):
            if text[i - 2] == first and text[i - 1] == second:
                res.append(text[i])
        
        return res