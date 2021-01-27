class Solution:
    def concatenatedBinary(self, n: int) -> int:
        M = 10 ** 9 + 7
        
        s = []
        for i in range(1, n+1):
            s.append(str(bin(i)[2:]))
        
        s = "".join(s)
        
        return int(s,2) % M