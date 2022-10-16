class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        n = len(S)
        
        def backtrack(i, s):
            if i == n: 
                res.append("".join(s))
                return
            
            if s[i].isalpha():
                s[i] = s[i].upper()
                backtrack(i+1, s)
                
                s[i] = s[i].lower()
                backtrack(i+1, s)
            
            else:
                backtrack(i+1, s)
        
        backtrack(0, list(S))
        
        return res