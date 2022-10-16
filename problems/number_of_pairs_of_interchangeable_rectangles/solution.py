class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        mp = collections.Counter()
        res = 0
        
        for x,y in rectangles:
            f = gcd(x, y)
            x //= f
            y //= f
            
            res += mp[(x, y)]
            mp[(x, y)] += 1
        
        return res
        