class Solution:
    def countAnagrams(self, s: str) -> int:
        M = 10 ** 9 + 7
        s = s.split(" ")
        N = len(s)
        res = 1

        for x in s:
            counter = Counter(x)
            n = factorial(len(x))

            for k, v in counter.items():
                n //= factorial(v)
            
            res = (res * n) % M
        
        return res
        