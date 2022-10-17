class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        res = 0
        
        for x in sentence:
            k = ord(x) - ord("a")
            
            if res & (1 << k) == 0:
                res ^= (1 << k)
        
        return res == (1 << 26) - 1