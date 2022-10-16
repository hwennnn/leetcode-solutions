class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        mp = {k:v for k,v in knowledge}
        res = []
        key = ""
        going = False
        
        for i,x in enumerate(s):
            if x == "(":
                going = True
            elif x == ")":
                going = False
                res.append(mp.get(key, "?"))
                key = ""
            elif going:
                key += x
            else:
                res.append(x)
        
        return "".join(res)