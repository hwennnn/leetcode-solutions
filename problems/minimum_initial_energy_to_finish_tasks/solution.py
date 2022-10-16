class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x:(x[0] - x[1]))
        
        res = curr = 0
        for cost, mmin in tasks:
            if curr < mmin:
                res += (mmin - curr)
                curr = mmin
            
            curr -= cost
        
        return res