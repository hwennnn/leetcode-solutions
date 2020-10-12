class Solution:
    def numWays(self, S: str) -> int:
        n = len(S)
        M = 10 ** 9 + 7
        ones = S.count("1")
        
        if ones % 3: return 0
        
        if ones == 0: return (((n-1) * (n-2)) // 2) % M
        
        ones /= 3
        first = second = c = 0
        
        for s in S:
            if s == "1":
                c += 1
            
            if c == ones:
                first += 1
            
            elif c == ones*2:
                second += 1
        
        return (first * second) % M