class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        N = len(s)
        M = 10 ** 9 + 7
        
        primes = set(["2", "3", "5", "7"])
        
        if s[0] not in primes or s[-1] in primes: return 0
        
        @cache
        def go(index, parts):
            if parts == 0 and index <= N: return 1
            if index >= N: return 0
            
            res = go(index + 1, parts)
            
            if s[index] in primes and s[index - 1] not in primes:
                res += go(index + minLength, parts - 1)
            
            return res % M
        
        return go(minLength, k - 1)