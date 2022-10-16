class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        
        for i in range(len(encoded)):
            res.append(res[-1] ^ encoded[i])
        
        return res