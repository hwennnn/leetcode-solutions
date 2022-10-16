class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        
        def generate(s):
            res = []
            
            if s == "0" or s[0] != "0": res.append(s)
            
            for i in range(1, len(s)):
                if (s[:i] == "0" or s[:i][0] != "0") and s[i:][-1] != "0":
                    res.append(s[:i] + "." + s[i:])
            
            return res
        
        res = []
        for i in range(2, len(s) - 1):
            left, right = generate(s[1:i]), generate(s[i:-1])

            for l, r in product(left, right):
                res.append("(" + l + ", " + r + ")")
        
        return res