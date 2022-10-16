class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, t: int) -> int:
        res = float('inf')
        
        for minutes in range(0, 100):
            curr = startAt
            seconds = t - minutes * 60
            
            if seconds < 0 or seconds > 99: continue
            
            p = [minutes // 10, minutes % 10, seconds // 10, seconds % 10]
            
            index = 0
            
            while index < 4 and p[index] == 0:
                index += 1
            
            costs = 0
            
            for i in range(index, 4):
                if p[i] != curr:
                    curr = p[i]
                    costs += moveCost
                
                costs += pushCost
            
            res = min(res, costs)
        
        return res