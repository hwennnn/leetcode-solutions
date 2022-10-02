class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        M = 10 ** 9 + 7
        
        @cache
        def go(dices, total):
            if dices == 0:
                return int(total == target)
            
            count = 0
            
            for x in range(1, k + 1):
                if x + total > target: break
                
                count += go(dices - 1, x + total)
                count %= M
            
            return count 
        
        return go(n, 0)
                
        