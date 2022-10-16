class Solution:
    def numberOfWays(self, s: str) -> int:
        rZero, rOne = s.count("0"), s.count("1")
        
        lZero = lOne = 0
        res = 0
        
        for x in s:
            if x == "1":
                lOne += 1
                res += lZero * rZero
                rOne -= 1
            else:
                lZero += 1
                res += lOne * rOne
                rZero -= 1

        return res