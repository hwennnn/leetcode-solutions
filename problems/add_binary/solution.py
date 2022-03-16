class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        n1, n2 = len(a), len(b)
        i, j = n1 - 1, n2 - 1
        res = []
        
        while i >= 0 or j >= 0 or carry > 0:
            if i >= 0:
                carry += int(a[i] == "1")
                i -= 1
                
            if j >= 0:
                carry += int(b[j] == "1")
                j -= 1
            
            res.append(str(carry % 2))
            carry //= 2
        
        return "".join(res[::-1])
        