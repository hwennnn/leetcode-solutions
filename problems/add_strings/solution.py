class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num2 = list(num2)
        res = ""
        carry = 0
        
        def val(x):
            return ord(x) - ord('0')
        
        while num1 or num2 or carry:
            if num1:
                carry += val(num1.pop())
            if num2:
                carry += val(num2.pop())
            
            res += str(carry % 10)
            carry //= 10
        
        return res[::-1]