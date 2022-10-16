class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [1] + [0] * 1023
        curr = res = 0
        
        for x in word:
            curr ^= (1 << ord(x) - ord('a'))
            res += count[curr]
            
            for bit in range(10):
                delta = 1 << bit
                res += count[curr ^ delta]
            
            count[curr] += 1
        
        return res