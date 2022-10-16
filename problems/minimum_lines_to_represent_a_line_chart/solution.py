class Solution:
    def minimumLines(self, stock: List[List[int]]) -> int:
        n = len(stock)
        
        if n == 1: return 0
        
        stock.sort(key = lambda x: x[0])
        dx = stock[0][0] - stock[1][0]
        dy = stock[0][1] - stock[1][1]
            
        res = 1
        
        for index in range(2, n):
            x, y = stock[index]
        
            dx1 = stock[index - 1][0] - stock[index][0]
            dy1 = stock[index - 1][1] - stock[index][1]  
            
            if dx1 * dy != dx * dy1:
                res += 1
                dx = dx1
                dy = dy1
        
        return res