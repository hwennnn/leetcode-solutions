class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        
        for i in range(100):
            for j in range(100):
                z = x ** i + y ** j
                if z <= bound:
                    res.add(z)
        
        return list(res)