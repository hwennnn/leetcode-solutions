class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        total = sum(matchsticks)
        if total % 4 != 0: return False
        target = total // 4
        matchsticks.sort(reverse = 1)
        
        @cache
        def go(mask):
            curr = 0
            
            for i in range(n):
                if (mask >> i) & 1 > 0:
                    curr += matchsticks[i]
            
            done, side = divmod(curr, target)
            
            if done == 3: return True
            
            for i in range(n):
                if (mask & (1 << i)) == 0:
                    if side + matchsticks[i] <= target and go(mask | (1 << i)):
                        return True
            
            return False
        
        return go(0)