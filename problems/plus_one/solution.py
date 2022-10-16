class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        digits[-1] += 1
        carry = 0
        
        for x in digits[::-1]:
            carry += x
            
            res.append(carry % 10)
            carry //= 10
        
        if carry > 0:
            res.append(carry)
        
        return res[::-1]