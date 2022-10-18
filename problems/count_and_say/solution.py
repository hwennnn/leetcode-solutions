class Solution:
    def countAndSay(self, n: int) -> str:
        
        @cache
        def go(i):
            if i == 1: return "1"
            
            prev = go(i - 1)
            res = ""
            
            for k, g in groupby(prev):
                res += str(len(list(g))) + k
            
            return res
    
        return go(n)