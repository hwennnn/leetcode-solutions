class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        a = b = 0
        
        for i in range(1, n - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == 'A':
                    a += 1
                else:
                    b += 1
        
        return a > b