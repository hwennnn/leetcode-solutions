class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        
        @cache
        def go(mask, curr, session):
            if mask == 0: return session
            
            res = float('inf')
            
            for i in range(n):
                if mask & (1 << i):
                    if curr + tasks[i] <= sessionTime:
                        res = min(res, go(mask ^ (1 << i), curr + tasks[i], session))
                    else:
                        res = min(res, go(mask ^ (1 << i), tasks[i], session + 1))
            
            return res
        
        return go((1 << n) - 1, 0, 1)