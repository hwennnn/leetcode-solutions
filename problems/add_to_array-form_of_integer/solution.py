class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        N = len(num)
        carry = k
        i = N - 1
        res = []

        while i >= 0 or carry > 0:
            if i >= 0:
                carry += num[i]
                i -= 1

            res.append(carry % 10)
            carry //= 10
        
        return res[::-1]