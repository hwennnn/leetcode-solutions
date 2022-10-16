class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(opened, closed, curr):
            if opened == closed == n:
                res.append(curr)
                return
            
            if closed < opened:
                backtrack(opened, closed + 1, curr + ")")
            
            if opened < n:
                backtrack(opened + 1, closed, curr + "(")
            
        backtrack(0, 0, "")
        return res