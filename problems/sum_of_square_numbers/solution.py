class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        s = set()

        for i in range(int(math.sqrt(c)) + 1):
            s.add(i * i)
        
        for x in s:
            if c - x in s:
                return True
        
        return False
        