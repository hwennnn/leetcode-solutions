class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        N = len(str(num))
        
        for x in range(num, num // 2 - 1, -1):
            if x + int(str(x)[::-1]) == num:
                return True
        
        return False