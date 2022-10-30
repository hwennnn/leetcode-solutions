class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        ns = list(str(n))
        N = len(ns)
        res = 10 ** (N + 1) - n
        
        def countDigits(x):
            digitSum = 0
            
            while x > 0:
                digitSum += x % 10
                x //= 10
            
            return digitSum
        
        def go(index, curr):
            nonlocal res
            
            if index == -1:
                ds = countDigits(curr)
                
                if ds <= target:
                    res = min(res, curr - n)
                
                return
            
            go(index - 1, curr)
            
            d = 10 ** (N - index)
            to_add = d - curr % d
            go(index - 1, curr + to_add)

        go(N - 1, n)
        return res
        