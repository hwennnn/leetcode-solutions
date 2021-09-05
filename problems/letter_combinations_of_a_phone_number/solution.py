class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        n = len(digits)
        res = []
        dic = {"2":"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}

        def backtrack(i, curr):
            if len(curr) == n:
                res.append(curr)
                return
            
            for j in range(i, n):
                for word in dic[digits[j]]:
                    backtrack(j + 1, curr + word)
        
        backtrack(0, "")
        
        return res