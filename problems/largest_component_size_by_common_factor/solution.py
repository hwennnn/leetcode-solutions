class DSU:
    def __init__(self, N):
        self.A = list(range(N))
    
    def find(self, x):
        if x != self.A[x]:
            self.A[x] = self.find(self.A[x])
        
        return self.A[x]
    
    def union(self, x, y):
        ux, uy = self.find(x), self.find(y)
        self.A[ux] = uy

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        primes = collections.defaultdict(list)
        dsu = DSU(n)
        
        def getPrimes(x):
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    return getPrimes(x // i) | set([i])
            
            return set([x])
        
        for i, x in enumerate(nums):
            primes_set = getPrimes(x)
            for q in primes_set:
                primes[q].append(i)
        
        for _, v in primes.items():
            for i in range(len(v) - 1):
                dsu.union(v[i], v[i + 1])
        
        return max(Counter([dsu.find(x) for x in range(n)]).values())
        
        
        