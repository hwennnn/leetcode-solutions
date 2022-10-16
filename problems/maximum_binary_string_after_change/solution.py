class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        if "0" not in binary: return binary
        
        idx = binary.index("0")
        
        res = []
        for _ in range(idx):
            res.append("1")
        
        ones = zeroes = 0
        for i in range(idx, len(binary)):
            if binary[i] == "1": ones += 1
            else: zeroes += 1
        
        while zeroes > 1:
            res.append("1")
            zeroes -= 1
        
        res.append("0")
        
        while ones > 0:
            res.append("1")
            ones -= 1
        
        return "".join(res)