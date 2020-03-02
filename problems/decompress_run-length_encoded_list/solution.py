class Solution:
    def decompressRLElist(self, A: List[int]) -> List[int]:
        
        return [x for a, b in zip(A[0::2], A[1::2]) for x in [b] * a]