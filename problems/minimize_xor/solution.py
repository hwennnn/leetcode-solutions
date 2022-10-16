class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bit = num2.bit_count()
        bits = [0] * (32)
        ans = 0

        for i in range(31, -1, -1):
            if num1 & (1 << i) > 0:
                if bit > 0:
                    bit -= 1
                    ans ^= (1 << i)
                    
                bits[i] += 1

        for i in range(32):
            if bit > 0 and bits[i] == 0:
                bits[i] += 1
                bit -= 1
                ans ^= (1 << i)
        
        return ans