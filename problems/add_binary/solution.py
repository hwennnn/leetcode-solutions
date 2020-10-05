class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        res = []
        
        while (i >= 0 or j >= 0 or carry):
            s = carry
            s += int(a[i]) if i >= 0 else 0
            s += int(b[j]) if j >= 0 else 0
            res.insert(0, str(s%2))
            carry = s//2
            i -= 1
            j -= 1
            
        return "".join(res)