class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = [True] * (n + 1)
        
        for prime in range(2, int(math.sqrt(n)) + 1):
            if primes[prime]:
                for composite in range(prime * prime, n + 1, prime):
                    primes[composite] = False
                    
        cnt = sum(primes[2:])

        return math.factorial(cnt) * math.factorial(n - cnt) % (10**9 + 7)
        