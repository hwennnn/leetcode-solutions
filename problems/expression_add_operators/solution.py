class Solution:
    def addOperators(self, s: str, target: int) -> List[str]:
        n = len(s)
        res = []
        
        def backtrack(i, path, curr, prev):
            if i == n:
                if curr == target:
                    res.append(path)
                return
            
            for j in range(i, n):
                if j > i and s[i] == '0': break
                num = int(s[i : j + 1])
                
                if i == 0:
                    backtrack(j + 1, path + str(num), curr + num, num)
                else:
                    backtrack(j + 1, path + "+" + str(num), curr + num, num)
                    backtrack(j + 1, path + "-" + str(num), curr - num, -num)
                    backtrack(j + 1, path + "*" + str(num), curr - prev + prev * num, prev * num)
                    
        backtrack(0, "", 0, 0)
        return res