class Solution:
    def interpret(self, C: str) -> str:
        
        n = len(C)
        i = 0
        res = []
        
        while i < n:
            if C[i] == "G":
                res.append("G")
                i += 1
            elif C[i] == "(" and i + 1 < n and C[i+1] == ")":
                res.append("o")
                i += 2
            elif C[i] == "(" and i + 3 < n and C[i:i+4] == "(al)":
                res.append("al")
                i += 4
            else:
                i += 1
            
        
        return "".join(res)
            