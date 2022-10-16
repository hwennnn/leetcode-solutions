class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        M = 10 ** 9 + 7
        res = 1
        
        canShare = defaultdict(int)
        canShare[delay] = 1
        
        toForget = defaultdict(int)
        toForget[forget] = 1

        propagate = 0
        
        for day in range(delay, n):
            propagate += canShare[day]    
            propagate -= toForget[day]
            
            res += propagate
            res -= toForget[day]
            res %= M
            
            canShare[day + delay] += propagate
            toForget[day + forget] += propagate
        
        return res % M