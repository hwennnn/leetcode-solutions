class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [True] * (right + 1)
        sieve[1] = False
        
        for i in range(2, int(math.sqrt(right)) + 1):
            if sieve[i]:
                for j in range(i * i, right + 1, i):
                    sieve[j] = False
            
        
        res = [inf, -1, -1]
        prev = -1
        for i in range(left, right + 1):
            if not sieve[i]: continue
            
            if prev == -1:
                prev = i
            else:
                diff = i - prev
                if diff < res[0]:
                    res = [diff, prev, i]
                
                prev = i
        
        return res[1:]
            