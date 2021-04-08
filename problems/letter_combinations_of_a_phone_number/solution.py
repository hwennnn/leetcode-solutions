class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        dic = {"2":"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        res = []
        
        self.dfs(dic, digits, 0, "", res)
        
        return res
    
    def dfs(self, dic, digits, index, curr, res):
        if len(curr) == len(digits):
            res.append(curr)
            return

        for c in dic[digits[index]]:
            self.dfs(dic, digits, index+1, curr+c, res)