class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        words = [word, word[::-1]]
        n = len(word)
        
        for B in board, zip(*board):
            for row in B:
                s = "".join(row).split('#')
                
                for word in words:
                    for z in s:
                        if len(z) == n and all(z[i] == word[i] or z[i] == ' ' for i in range(n)):
                            return True
        
        return False