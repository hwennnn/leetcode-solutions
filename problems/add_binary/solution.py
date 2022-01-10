class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = []
        
        for x, y in zip_longest(a[::-1], b[::-1], fillvalue = "0"):
            curr = carry + int(x) + int(y)
            carry, value = divmod(curr, 2)
            res.append(str(value))
            
        if carry:
            res.append("1")
        
        return "".join(res)[::-1]