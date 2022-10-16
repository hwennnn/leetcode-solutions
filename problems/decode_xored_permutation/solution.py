class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        curr = start = 0
        
        for i in range(1, len(encoded)+2):
            start ^= i
        
        for x in encoded:
            curr ^= x
            start ^= curr
        
        res = [start]
        for x in encoded:
            res.append(res[-1] ^ x)
        
        return res