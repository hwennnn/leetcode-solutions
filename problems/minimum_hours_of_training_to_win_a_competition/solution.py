class Solution:
    def minNumberOfHours(self, A: int, B: int, energy: List[int], experience: List[int]) -> int:
        res = 0
        
        for a, b in zip(energy, experience):
            if a >= A:
                res += a - A + 1
                A += a - A + 1
            
            if b >= B:
                res += b - B + 1
                B += b - B + 1
                
            A -= a
            B += b
        
        return res