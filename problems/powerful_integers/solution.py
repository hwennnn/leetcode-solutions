class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        
        i = 1
        while i < bound:
            j = 1
            while i + j <= bound:
                res.add(i + j)
                if y == 1: break
                j *= y
            
            if x == 1: break
            i *= x
        
        return list(res)