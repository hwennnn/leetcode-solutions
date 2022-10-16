class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n & 1: res.append(0)
            
        for i in range(-1000,-1000+n//2):
            res.append(i)


        for i in range(1000, 1000 - n//2, -1):
            res.append(i)

        
        return res
            