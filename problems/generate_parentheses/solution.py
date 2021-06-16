class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(curr = "", opened = 0, closed = 0):
            if opened == closed == n:
                res.append(curr)
                return
            
            if closed < opened:
                backtrack(curr + ")", opened, closed + 1)
            
            if opened < n:
                backtrack(curr + "(", opened + 1, closed)

        backtrack()
        
        return res