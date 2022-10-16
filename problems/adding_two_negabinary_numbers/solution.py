class Solution:
    def addNegabinary(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        carry = 0
        
        while A or B or carry:
            carry += (A or [0]).pop() + (B or [0]).pop()
            res.append(carry & 1)
            carry = -(carry >> 1)
        
        while len(res) > 1 and res[-1] == 0: res.pop()
        
        return res[::-1]